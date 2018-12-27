from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DecimalField, SelectField, DateTimeField, TimeField, IntegerField, SelectMultipleField, DateField, FileField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email!')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=40, message='Your password must be at least 6 characters long and a mix of letters, numbers and special symbols.')])

class RecoverPasswordForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email!')])

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[InputRequired(), Length(min=6, max=40, message='Your password must be at least 6 characters long and a mix of letters, numbers and special symbols.')])
    password2 = PasswordField('New Password', validators=[InputRequired(), Length(min=6, max=40, message='Your password must be at least 6 characters long and a mix of letters, numbers and special symbols.')])

class AddUserForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    surname = StringField('Surname', validators=[])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email!')])
    system_role = SelectField('System Role', coerce=int)
    holidays_quota = IntegerField('Holidays quota', validators=[InputRequired()])

class RequestHolidaysForm(FlaskForm):
    date_from = DateField('From', format='%d-%m-%Y', validators=[InputRequired()], id='datepicker1')
    date_to = DateField('To', format='%d-%m-%Y', validators=[InputRequired()], id='datepicker2')
    comment = TextAreaField('Comment', validators=[])

class UpdateHolidaysRequest(FlaskForm):
    request = SelectField('Request ID', coerce=int)
    status = SelectField('Status', choices=[('Select one','Select one'),('Approved','Approved'), ('Pending','Pending'),('Declined','Declined'),('Cancelled','Cancelled')])
    manager_comment = TextAreaField('Comment - will be added to the email')
