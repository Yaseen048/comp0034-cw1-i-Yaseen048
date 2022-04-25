from flask import Blueprint, render_template
from flask_login import login_required
from flask_app import login_manager
from flask_app.models import User
from flask_app.chat.forms import MessageForm

chat_bp = Blueprint('chat', __name__)

@login_manager.user_loader
def load_user(user_id):
    """ Takes a user ID and returns a user object or None if the user does not exist"""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@chat_bp.route('/view')
@login_required
def view():
    return render_template('chat.html', title = 'chat')

@chat_bp.route('/message')
@login_required
def message():
    message_form = MessageForm()
    