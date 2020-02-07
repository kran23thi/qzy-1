from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, Length, email, equal_to


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[data_required(),Length(min=2,max=20)])
    email = StringField('Email', validators=[data_required(), email()])
    password =PasswordField('Password', validators=[data_required()])
    confirm_password = PasswordField('Confirm Password', validators=[data_required(),equal_to('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[data_required(), email()])
    password =PasswordField('Password', validators=[data_required()])
    remember =BooleanField('Remember me')
    submit = SubmitField('Login')


