# flake8: noqa F401
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
)
from flask_login import login_required, current_user
import sqlalchemy as sa
from flask import current_app as app
from app.controllers import create_pagination
from app import models as m, db
from app import forms as f
from app.logger import log


report_blueprint = Blueprint("report", __name__, url_prefix="/report")


@report_blueprint.route("/all", methods=["GET", "POST"])
@login_required
def dashboard():
    views_filter = "NA"
    type_filter = "All"
    make_filter = "All"
    model_filter = "All"
    price_lower = None
    price_upper = None
    start_date = None
    end_date = None
    date_received = None
    if request.method == "POST":
        views_filter = request.form.get("views_filter")
        type_filter = request.form.get("type_filter")
        make_filter = request.form.get("make_filter")
        model_filter = request.form.get("model_filter")
        price_lower = request.form.get("price-lower")
        price_upper = request.form.get("price-upper")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        date_received = request.form.get("date_received")

    if views_filter == "Asc":
        order_by = m.Label.views.asc()
    elif views_filter == "Desc":
        order_by = m.Label.views.desc()
    else:
        order_by = m.Label.id

    query = (
        m.Label.select().where(m.Label.user_id == current_user.id).order_by(order_by)
    )
    count_query = (
        sa.select(sa.func.count())
        .select_from(m.Label)
        .where(m.Label.user_id == current_user.id)
    )

    if start_date and end_date:
        start_date = datetime.strptime(start_date, "%m/%d/%Y")
        end_date = datetime.strptime(end_date, "%m/%d/%Y")
        query = query.where(sa.func.DATE(m.Label.date_received) >= start_date)
        query = query.where(sa.func.DATE(m.Label.date_received) <= end_date)
    elif date_received:
        date_received = datetime.strptime(date_received, "%m/%d/%Y").date()
        query = query.where(sa.func.DATE(m.Label.date_received) == date_received)

    if make_filter and make_filter != "All":
        query = query.where(m.Label.make == make_filter)
        count_query = count_query.where(m.Label.make == make_filter)
    if model_filter and model_filter != "All":
        query = query.where(m.Label.vehicle_model == model_filter)
        count_query = count_query.where(m.Label.vehicle_model == model_filter)
    if type_filter and type_filter != "All":
        query = query.where(m.Label.type_of_vehicle == type_filter)
        count_query = count_query.where(m.Label.type_of_vehicle == type_filter)
    if views_filter == "Asc":
        query = query.order_by(m.Label.views.asc())
    elif views_filter == "Desc":
        query = query.order_by(m.Label.views.desc())
    if price_lower:
        query = query.where(m.Label.price >= price_lower)
        count_query = count_query.where(m.Label.price >= price_lower)
    if price_upper:
        query = query.where(m.Label.price <= price_upper)
        count_query = count_query.where(m.Label.price <= price_upper)

    pagination = create_pagination(total=db.session.scalar(count_query))
    labels = (
        db.session.execute(
            query.offset((pagination.page - 1) * pagination.per_page).limit(
                pagination.per_page
            )
        )
        .scalars()
        .all()
    )
    types = list(
        set(
            [
                label.type_of_vehicle
                for label in db.session.scalars(
                    m.Label.select().where(m.Label.user_id == current_user.id)
                ).all()
            ]
        )
    )
    makes = list(
        set(
            [
                label.make
                for label in db.session.scalars(
                    m.Label.select().where(m.Label.user_id == current_user.id)
                ).all()
            ]
        )
    )
    if make_filter and make_filter != "All":
        models = list(
            set(
                [
                    label.vehicle_model
                    for label in db.session.scalars(
                        m.Label.select()
                        .where(m.Label.user_id == current_user.id)
                        .where(m.Label.make == make_filter)
                    ).all()
                ]
            )
        )
    else:
        models = list(
            set(
                [
                    label.vehicle_model
                    for label in db.session.scalars(
                        m.Label.select().where(m.Label.user_id == current_user.id)
                    ).all()
                ]
            )
        )

    return render_template(
        "report/dashboard.html",
        labels=labels,
        makes=makes,
        make_filter=make_filter,
        models=models,
        model_filter=model_filter,
        types=types,
        type_filter=type_filter,
        views_filter=views_filter,
        page=pagination,
    )


@report_blueprint.route("/get_models", methods=["POST"])
@login_required
def get_models():
    make = request.json.get("makeSelected")
    labels = db.session.scalars(
        m.Label.select()
        .where(m.Label.user_id == current_user.id)
        .where(m.Label.make == make)
    ).all()
    models = list(set([label.vehicle_model for label in labels]))
    return {"models": models}


@report_blueprint.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    ...
    return redirect(url_for("report.get_all"))