from flask import Blueprint, redirect, url_for
from sqlalchemy import true
from flask_app.auth.forms import SignupForm, LoginForm
from flask import render_template, flash
from sqlalchemy.exc import IntegrityError
from flask_app import db
from flask_app.models import User



auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth')
def index():
    return "This is the authentication section of the web app"

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash (f"Hello, {user.first_name}. You are signed up.")
        except IntegrityError:
            db.session.rollback()
            flash(f"There was an error. Unable to register {form.email.data}.",'Error')
            return redirect(url_for('auth.signup'))
        return redirect(url_for('main.index'))
    return render_template('signup.html', title='Sign Up', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    #validation code
    if login_form.validate_on_submit():
        #user = User(first_name='first_name', last_name='last_name', email=login_form.email.data)
        #user.set_password(login_form.password.data)
        flash ("Hello, You are logged in.")
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Login', form=login_form)
