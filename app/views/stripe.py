import stripe
import os
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    jsonify,
)
from flask_login import current_user
from app import models as m, db
from app import forms as f
from app.logger import log

stripe_blueprint = Blueprint("stripe", __name__, url_prefix="/stripe")

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")


@stripe_blueprint.route("/webhook", methods=["GET", "POST"])
def webhook():
    event = None
    payload = request.data
    sig_header = request.headers["STRIPE_SIGNATURE"]

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, os.environ.get("ENDPOINT_SECRET")
        )
    except Exception as e:
        raise e

    if event["type"] == "customer.subscription.created":
        response = event["data"]["object"]
        user: m.User = db.session.scalar(
            m.User.select().where(m.User.stripe_customer_id == response.customer)
        )
        product: m.StripeProduct = db.session.scalar(
            m.StripeProduct.select().where(
                m.StripeProduct.stripe_product_id == response.plan.product
            )
        )
        if not user:
            log(log.ERROR, "User [%s] not found", response.customer)
            return jsonify(success=False), 404
        if not product:
            log(log.ERROR, "Product [%s] not found", response.plan.product)
            return jsonify(success=False), 404
        subscription = m.Subscription(
            stripe_subscription_id=response.id,
            user_id=user.id,
            product_id=product.id,
            current_period_start=response.current_period_start,
            current_period_end=response.current_period_end,
            is_active=True,
        )
        subscription.save()
        user.activated = True
        user.save()
        log(log.INFO, "Subscription [%s] created ", subscription.stripe_subscription_id)
    elif event["type"] == "customer.subscription.updated":
        response = event["data"]["object"]
        response = event["data"]["object"]
        subscription: m.Subscription = db.session.scalar(
            m.Subscription.select().where(
                m.Subscription.stripe_subscription_id == response.id
            )
        )
        subscription.is_active = not response.cancel_at_period_end
        subscription.current_period_start = response.current_period_start
        subscription.current_period_end = response.current_period_end
        subscription.save()
        log(log.INFO, "Subscription [%s] updated ", subscription.stripe_subscription_id)
    elif event["type"] == "customer.subscription.deleted":
        response = event["data"]["object"]
        user: m.User = db.session.scalar(
            m.User.select().where(m.User.stripe_customer_id == response.customer)
        )
        subscription: m.Subscription = db.session.scalar(
            m.Subscription.select().where(
                m.Subscription.stripe_subscription_id == response.id
            )
        )
        subscription.is_active = False
        subscription.save()
        log(
            log.INFO,
            "Subscription [%s] cancelled ",
            subscription.stripe_subscription_id,
        )
        user.activated = False
        user.save()
    else:
        log(log.ERROR, "Unhandled event type %s", event["type"])

    return jsonify(success=True)


@stripe_blueprint.route("/subscription", methods=["GET", "POST"])
def subscription():
    form: f.SubscriptionPlanForm = f.SubscriptionPlanForm()
    if form.validate_on_submit():
        current_user.plan = form.selected_plan.data
        current_user.save()
        log(log.INFO, "Pay plan is chosen. User: [%s]", current_user)
        if current_user.plan == m.UsersPlan.advanced:
            log(
                log.INFO, "User [%s] is advanced. Redirect to logo upload", current_user
            )
            return redirect(
                url_for("auth.logo_upload", user_unique_id=current_user.unique_id)
            )
        log(log.INFO, "User [%s] is basic. Redirect to auth.payment", current_user)
        return redirect(url_for("auth.payment", user_unique_id=current_user.unique_id))
    elif form.is_submitted():
        log(log.ERROR, "Form submitted error: [%s]", form.errors)
        flash("Something went wrong. Please try again later.", "danger")
        return redirect(url_for("stripe.subscription"))

    flash("You are successfully changed your plan!", "success")
    return render_template(
        "user/subscription_update.html",
        user=current_user,
        form=form,
        user_unique_id=current_user.unique_id,
    )


@stripe_blueprint.route("/portal", methods=["GET"])
def portal():
    try:
        log(log.INFO, "User [%s] is going to stripe portal", current_user)
        portal_response = stripe.billing_portal.Session.create(
            customer=current_user.stripe_customer_id,
        )
    except Exception as e:
        log(log.ERROR, "stripe_portal: %s", e)
        flash("Something went wrong. Please try again later.", "danger")

    log(log.INFO, "User [%s] is redirected to stripe portal", current_user)
    return redirect(portal_response.url, code=302)
