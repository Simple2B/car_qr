# flake8: noqa F401

from datetime import date
from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
    session,
    request,
)
import sqlalchemy as sa
from flask_login import login_required, current_user
from app.controllers import role_required
from app import models as m, db
from app import mail
from flask_mail import Message
from flask import current_app as app
from app import forms as f
from app import schema as s
from app.controllers.pagination import create_pagination
from app.logger import log

from .utils import get_canada_provinces, get_us_states

service = Blueprint("service", __name__, url_prefix="/services")


@service.route("/", methods=["GET"])
@login_required
@role_required([m.UsersRole.admin, m.UsersRole.dealer])
def get_all():
    log(log.INFO, "Getting all services")

    admin_ids = db.session.scalars(
        sa.select(m.User.id).where(m.User.role == m.UsersRole.admin)
    ).all()

    where_stmt = sa.and_(
        m.User.role == m.UsersRole.service,
        m.User.activated,
        m.User.deleted.is_(False),
        m.User._creator_id.in_(admin_ids + [current_user.id]),
    )

    query = sa.select(m.User).where(where_stmt).order_by(m.User.created_at.desc())
    count_query = sa.select(sa.func.count()).where(where_stmt).select_from(m.User)

    pagination = create_pagination(total=db.session.scalar(count_query))

    return render_template(
        "service/services.html",
        services=db.session.execute(
            query.offset((pagination.page - 1) * pagination.per_page).limit(
                pagination.per_page
            )
        ).scalars(),
        page=pagination,
    )


@service.route("/add-modal", methods=["GET"])
@login_required
@role_required([m.UsersRole.admin, m.UsersRole.dealer])
def add_modal():
    """htmx"""
    form = f.ServiceForm()
    form.province.choices = get_canada_provinces()

    return render_template(
        "service/add_modal.html",
        form=form,
    )


@service.route("/add", methods=["POST"])
@login_required
@role_required([m.UsersRole.admin, m.UsersRole.dealer])
def add():
    form = f.ServiceForm()
    if not form.validate_on_submit():
        log(log.INFO, f"Invalid form data [{form.format_errors}]")
        flash(f"Invalid form data [{form.format_errors}]", "danger")
        return redirect(url_for("service.get_all"))

    user = m.User(
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        email=form.email.data,
        name_of_dealership=form.name.data,
        phone=form.phone.data,
        address_of_dealership=form.address.data,
        country=form.country.data,
        province=form.province.data,
        city=form.city.data,
        postal_code=form.postal_code.data,
        role=m.UsersRole.service,
        activated=True,
        creator_id=current_user.id,
        password=form.password.data,
    ).save()
    msg = Message(
        subject="Invitation to Auto QR Code",
        sender=app.config["MAIL_DEFAULT_SENDER"],
        recipients=[user.email],
    )
    url = url_for(
        "auth.login",
        _external=True,
    )

    msg.html = render_template(
        "email/service_invite.html",
        user=user,
        url=url,
        password=form.password.data,
    )
    mail.send(msg)

    return redirect(url_for("service.get_all"))


@service.route("/<service_unique_id>/edit-modal", methods=["GET"])
@login_required
@role_required([m.UsersRole.admin, m.UsersRole.dealer])
def edit_modal(service_unique_id: str):
    """htmx"""

    service = db.session.scalar(
        sa.select(m.User).where(
            m.User.unique_id == service_unique_id, m.User.role == m.UsersRole.service
        )
    )

    if not service or service.creator_id != current_user.id:
        log(log.INFO, f"Service not found or not allowed to edit [{service_unique_id}]")
        return render_template(
            "toast.html", message="Service not found", toast_type="danger"
        )

    form = f.EditServiceForm()

    form.province.choices = get_canada_provinces()
    if service.country == s.Country.US.name:
        form.province.choices = get_us_states()

    form.first_name.data = service.first_name
    form.last_name.data = service.last_name
    form.service_unique_id.data = service.unique_id
    form.name.data = service.name_of_dealership
    form.email.data = service.email
    form.phone.data = service.phone
    form.address.data = service.address_of_dealership
    form.city.data = service.city
    form.postal_code.data = service.postal_code

    return render_template(
        "service/edit_modal.html",
        form=form,
        service=service,
    )


@service.route("/edit", methods=["POST"])
@login_required
@role_required([m.UsersRole.admin, m.UsersRole.dealer])
def edit():
    form = f.EditServiceForm()
    if not form.validate_on_submit():
        log(log.INFO, f"Invalid form data [{form.format_errors}]")
        flash(f"Invalid form data [{form.format_errors}]", "danger")
        return redirect(url_for("service.get_all"))

    service = db.session.scalar(
        sa.select(m.User).where(
            m.User.unique_id == form.service_unique_id.data,
            m.User.role == m.UsersRole.service,
        )
    )

    if not service or service.creator_id != current_user.id:
        log(
            log.INFO,
            f"Service not found or not allowed to edit [{form.service_unique_id.data}]",
        )
        flash("Service not found", "danger")
        return redirect(url_for("service.get_all"))

    service.first_name = form.first_name.data
    service.last_name = form.last_name.data
    service.name_of_dealership = form.name.data
    service.email = form.email.data
    service.phone = form.phone.data
    service.address_of_dealership = form.address.data
    service.country = form.country.data
    service.province = form.province.data
    service.city = form.city.data
    service.postal_code = form.postal_code.data

    if form.new_password.data:
        service.password = form.new_password.data

    db.session.commit()

    return redirect(url_for("service.get_all"))


@service.route("/records", methods=["GET"])
@login_required
@role_required([m.UsersRole.service])
def records():
    log(log.INFO, "Getting all records")

    query = sa.select(m.ServiceRecord).where(
        m.ServiceRecord.service_id == current_user.id
    )

    count_query = (
        sa.select(sa.func.count())
        .where(m.ServiceRecord.service_id == current_user.id)
        .select_from(m.ServiceRecord)
    )

    pagination = create_pagination(total=db.session.scalar(count_query))

    return render_template(
        "service/records.html",
        records=db.session.execute(
            query.offset((pagination.page - 1) * pagination.per_page).limit(
                pagination.per_page
            )
        ).scalars(),
        page=pagination,
    )


@service.route("/confirm_oil_change", methods=["GET", "POST"])
@login_required
@role_required([m.UsersRole.service])
def confirm_oil_change():
    sticker_id = session.get("sticker_id")
    log(log.INFO, "Approved oil change [%s]", sticker_id)
    if not sticker_id:
        log(log.INFO, "Sticker ID not found [%s]", sticker_id)
        session.pop("sticker_id", default=None)
        flash("Car not found", "danger")
        return redirect(url_for("service.records"))

    label = db.session.scalar(
        sa.select(m.Label).where(m.Label.sticker_id == sticker_id)
    )
    if not label or not label.oil_not_changed:
        log(log.INFO, "Label not found")
        session.pop("sticker_id", default=None)
        flash("Car not found", "danger")
        return redirect(url_for("service.records"))

    oil_change = db.session.scalar(
        sa.select(m.OilChange).where(
            m.OilChange.sale_rep_id == label.sale_report.id,
            m.OilChange.is_done.is_(False),
            sa.func.DATE(m.OilChange.date) <= date.today(),
        )
    )
    if not oil_change:
        log(log.INFO, "Oil change not found")
        session.pop("sticker_id", default=None)
        flash("Oil change record not found", "danger")
        return redirect(url_for("service.records"))

    if request.method == "GET":
        return render_template(
            "service/confirm_oil_change.html",
        )

    log(log.INFO, "Confirming oil change")
    oil_change.is_done = True
    session.pop("sticker_id", default=None)

    record = m.ServiceRecord(
        service_id=current_user.id,
        label_id=label.id,
        oil_change_id=oil_change.id,
        name="Oil Change",
    )

    db.session.add(record)
    db.session.commit()
    flash("Oil change confirmed", "success")

    sale_rep = oil_change.sale_rep
    seller = sale_rep.seller
    buyer = sale_rep.buyer
    label = sale_rep.label

    msg = Message(
        subject="Oil Change Confirmation",
        sender=app.config["MAIL_DEFAULT_SENDER"],
        recipients=[seller.email],
    )
    msg.html = render_template(
        "email/did_oil_change.html",
        user=seller,
        buyer=buyer,
        label=label,
        service_name=current_user.name_of_dealership.title(),
        created_at=record.created_at,
    )
    mail.send(msg)

    return redirect(url_for("service.records"))
