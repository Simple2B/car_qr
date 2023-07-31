from datetime import datetime
from flask_wtf import FlaskForm
from flask_login import current_user
from app import db
from app import models as m


# Paste in forms in html templates: {{ form_hidden_tag() }}
def form_hidden_tag():
    form = FlaskForm()
    return form.hidden_tag()


def time_delta(created_at: datetime):
    return (datetime.utcnow() - created_at).days


def days_active(date_received: datetime, date_deactivated: datetime):
    return (date_deactivated - date_received).days


def labels_in_cart():
    if isinstance(current_user, m.User):
        labels = db.session.scalars(
            m.Label.select()
            .where(m.Label.user_id == current_user.id)
            .where(m.Label.status == m.LabelStatus.cart)
        ).all()
        return len(labels)
    return 0
