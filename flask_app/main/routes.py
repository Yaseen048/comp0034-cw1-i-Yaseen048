from flask import Blueprint, render_template, flash
from flask_login import current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if not current_user.is_anonymous:
        name = current_user.first_name
        flash(f'Hello {name}, you are now logged in')
    return render_template('index.html', title = "Home")