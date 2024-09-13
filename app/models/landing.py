from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from flask_wtf.recaptcha import RecaptchaField

from wtforms.validators import DataRequired, Email, Length



class LandingForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=1, max=128)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = StringField(
        "Message", validators=[DataRequired(), Length(min=1, max=256)]
    )
    submit = SubmitField("Submit")
    recaptcha = RecaptchaField()
