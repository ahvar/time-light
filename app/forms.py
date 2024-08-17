"""
User Login Form

NOTE:
    -----------
    Extensions:
    -----------
    The four classes that represent the field types that I'm using for this form are imported directly from the WTForms package.
    Flask-WTF extension does not provide customized versions.

    -----------
    Validators:
    -----------
    The optional validators argument is used to attach validation behaviors to fields. The DataRequired validator checks that the
    field is not submitted empty.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
