from flask import Blueprint, redirect, url_for
from flask_app.auth.forms import SignupForm, LoginForm
from flask import render_template, flash


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth')
def index():
    return "This is the authentication section of the web app"

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.first_name.data
        flash (f"Hello, {name}. You are signed up.")
        return redirect(url_for('main.index'))
    return render_template('signup.html', title='Sign Up', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #validation code
    return render_template('login.html', title='Login', form=form)
