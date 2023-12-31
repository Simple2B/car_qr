import os
import subprocess
from flask import Flask, render_template
from flask_login import LoginManager
from pyecharts.globals import CurrentConfig
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate
from flask_mail import Mail
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from app.logger import log
from .database import db

login_manager = LoginManager()
migration = Migrate()
mail = Mail()
scheduler = BackgroundScheduler()


def subscriptions_expiration_notifier():
    flask_proc = subprocess.Popen(["flask", "subscriptions-check"])
    flask_proc.communicate()


def create_app(environment="development"):
    from config import config
    from app.views import (
        main_blueprint,
        auth_blueprint,
        user_blueprint,
        dealer_blueprint,
        report_blueprint,
        stripe_blueprint,
        location_blueprint,
    )
    from app import models as m

    # Instantiate app.
    app = Flask(__name__)

    # Set app config.
    env = os.environ.get("APP_ENV", environment)
    configuration = config(env)
    app.config.from_object(configuration)
    configuration.configure(app)
    log(log.INFO, "Configuration: [%s]", configuration.ENV)

    # Set up extensions.
    db.init_app(app)
    migration.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    CurrentConfig.ONLINE_HOST = "/static/js/"
    if not app.config["TESTING"]:
        JOB_STORES = {
            "default": SQLAlchemyJobStore(url=configuration.ALCHEMICAL_DATABASE_URL)
        }
        scheduler.configure(jobstores=JOB_STORES)
        scheduler.start()
        job = scheduler.get_job("subscriptions_expiration_notifier")
        if not job:
            scheduler.add_job(
                id="subscriptions_expiration_notifier",
                func=subscriptions_expiration_notifier,
                trigger="cron",
                hour=configuration.SUBSCRIPTIONS_EXPIRATION_CHECK_HOUR,
                minute=0,
                second=0,
                replace_existing=True,
            )

    # Register blueprints.
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(dealer_blueprint)
    app.register_blueprint(report_blueprint)
    app.register_blueprint(stripe_blueprint)
    app.register_blueprint(location_blueprint)

    # Set up flask login.
    @login_manager.user_loader
    def get_user(id: int):
        query = m.User.select().where(m.User.id == int(id))
        return db.session.scalar(query)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    login_manager.anonymous_user = m.AnonymousUser

    # Error handlers.
    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template("error.html", error=exc), exc.code

    # Jinja globals
    from app.controllers.jinja_globals import (
        form_hidden_tag,
        time_delta,
        days_active,
        labels_in_cart,
        price_format,
        get_user_logo,
        gift_logo,
        years,
        get_gift_url,
    )

    app.jinja_env.globals["form_hidden_tag"] = form_hidden_tag
    app.jinja_env.globals["time_delta"] = time_delta
    app.jinja_env.globals["days_active"] = days_active
    app.jinja_env.globals["labels_in_cart"] = labels_in_cart
    app.jinja_env.globals["price_format"] = price_format
    app.jinja_env.globals["get_user_logo"] = get_user_logo
    app.jinja_env.globals["gift_logo"] = gift_logo
    app.jinja_env.globals["years"] = years
    app.jinja_env.globals["get_gift_url"] = get_gift_url

    return app
