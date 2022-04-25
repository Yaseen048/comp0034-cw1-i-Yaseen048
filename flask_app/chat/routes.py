from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from flask_app import login_manager, db
from flask_app.models import User
from flask_app.chat.forms import MessageForm
from flask_app.models import Message

from sqlalchemy.exc import IntegrityError


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
    uploaded_messages = Message.query.all()

    return render_template('chat.html', title = 'chat', 
        uploaded_messages = uploaded_messages)

@chat_bp.route('/message', methods = ['GET', 'POST'])
@login_required
def message():
    message_form = MessageForm()
    if message_form.validate_on_submit():
        message = Message(author_id = current_user.id, message_text = message_form.message.data)
        try:
            db.session.add(message)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash(f"There was an error. Unabke to upload message",'Error')
            return redirect(url_for('chat.message'))
        return redirect(url_for('chat.view'))
    return render_template('write_message.html', title='Write message', form=message_form)