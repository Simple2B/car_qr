from flask import (
    current_app as app,
    render_template,
    redirect,
    url_for,
    Blueprint,
    flash,
)
from flask_login import current_user
from flask_mail import Message, Mail
from app import models as m, db
from app.logger import log


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    return redirect(url_for("main.landing"))


@main_blueprint.route("/no-content")
def no_content():
    return "", 200


@main_blueprint.route("/l/<sticker_id>")
def redirect_to_outer_url(sticker_id: str):
    log(log.INFO, "Current user: [%s]", current_user)
    label: m.Label = db.session.scalar(
        m.Label.select().where(m.Label.sticker_id == sticker_id)
    )
    if not label:
        log(log.WARNING, "Label not found. Sticker ID: [%s]", sticker_id)
        return redirect(url_for("main.landing"))

    log(log.INFO, "Unauthorized user. Counting views. Label: [%s]", label)
    log(log.INFO, "views before: [%s]", label.views)
    view = m.LabelView(label_id=label.id)
    db.session.add(view)
    db.session.commit()
    log(log.INFO, "views after: [%s]", label.views)

    # if label.oil_not_changed:
    #     log(log.INFO, "Label oil_not_changed: [%s]", label)
    #     logout_user()
    #     session.clear()
    #     session["sticker_id"] = sticker_id
    #     return redirect(url_for("auth.login"))

    if label.gift:
        log(log.INFO, "Redirecting to gift page. Label: [%s]", label)
        return redirect(url_for("labels.gift", sticker_id=sticker_id))

    log(log.INFO, "Redirecting to outer URL. Label: [%s]", label)
    return redirect(label.url)


@main_blueprint.route("/landing", methods=["GET", "POST"])
def landing():
    if current_user.is_authenticated:
        if current_user.role.value == "admin":
            return redirect(url_for("user.get_all"))
        elif current_user.role.value == "dealer":
            return redirect(
                url_for("user.account", user_unique_id=current_user.unique_id)
            )
    mail = Mail()
    form = m.LandingForm()
    if form.validate_on_submit():
        msg = Message(
            subject="New Customer",
            sender=app.config["MAIL_DEFAULT_SENDER"],
            recipients=[app.config.get("ADMIN_EMAIL")],
        )

        msg.html = render_template(
            "email/new_customer.htm",
            name=form.name.data,
            email=form.email.data,
            message=form.message.data,
        )
        # mail.send(msg)

        flash("Your credentials are sent to admin", "success")
        return redirect(url_for("main.landing"))
    elif form.is_submitted():
        log(log.WARNING, "Form submitted error: [%s]", form.errors)
        flash("The given data was invalid.", "danger")
    return render_template(
        "landing.html",
        form=form,
        RECAPTCHA_PUBLIC_KEY=app.config["RECAPTCHA_PUBLIC_KEY"],
    )
