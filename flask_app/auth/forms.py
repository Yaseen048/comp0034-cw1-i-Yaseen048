from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from flask_app.models import User

class SignupForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired()])
    last_name = StringField(label='Last name', validators=[DataRequired()])
    email = EmailField(label='Email address', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    password_repeat = PasswordField(label='Repeat Password',
                                validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
                        
    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('An account is already registered for that email address')

class LoginForm(FlaskForm):
    email = EmailField(label='Email address', validators=[DataRequired()])
    form_password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField('Login in')

    def validate_login_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('This email is not registered')
    
    def validate_login_password(self, email, form_password):
        user = User.query.filter_by(email=email.data).first()
        if not user.check_password(form_password):
            raise ValidationError('Incorrect Password')