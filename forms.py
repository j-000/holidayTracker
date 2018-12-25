from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DecimalField, SelectField, DateTimeField, TimeField, IntegerField, SelectMultipleField, DateField, FileField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email!')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=40, message='Your password must be at least 6 characters long and a mix of letters, numbers and special symbols.')])
