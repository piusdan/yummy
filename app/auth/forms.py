from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Length, Optional, Email, Regexp, EqualTo

from app.models import Users


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Optional(), Length(1, 64),
    Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
    'Usernames must have only letters, '
    'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    confirm = BooleanField('I agree to terms and conditions')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if field.data:
            if Users.filter_by(email=field.data).first():
                raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if Users.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
