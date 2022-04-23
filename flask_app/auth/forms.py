import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class SignupForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired()])
    last_name = StringField(label='Last name', validators=[DataRequired()])
    email = EmailField(label='Email address', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    password_repeat = PasswordField(label='Repeat Password',
                                validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
                        

class LoginForm(FlaskForm):
    email = EmailField(label='Email address', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField('Login in')
