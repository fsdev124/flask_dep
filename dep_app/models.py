from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired, ValidationError, Email
from wtforms.widgets import HTMLString, html_params, Select

class SignupForm(FlaskForm):
    username = TextField(u'Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField(u'Sign In')