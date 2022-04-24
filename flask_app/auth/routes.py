from os import abort
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user
from flask_app.auth.forms import SignupForm, LoginForm

from sqlalchemy.exc import IntegrityError
from flask_app import db, login_manager, request
from flask_app.models import User
from urllib.parse import urlparse, urljoin

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    """ Takes a user ID and returns a user object or None if the user does not exist"""
    if user_id is not None:
        return User.query.get(user_id)
    return None

def is_safe_url(target):
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))
    return redirect_url.scheme in ('http', 'https') and host_url.netloc == redirect_url.netloc


def get_safe_redirect():
    url = request.args.get('next')
    if url and is_safe_url(url):
        return url
    url = request.referrer
    if url and is_safe_url(url):
        return url
    return '/'



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
        user = User.query.filter_by(email=login_form.email.data).first()
        login_user(user)
        next = request.args.get("next")
        if not is_safe_url(next):
            return abort(400)
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Login', form=login_form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))