from flask_wtf import FlaskForm
from wtforms import StringField  #, SubmitField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    message = StringField(label = 'Message', validators=[DataRequired()])