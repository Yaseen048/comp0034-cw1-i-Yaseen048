from flask_app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    messages = db.relationship("Message", backref = db.backref('user'))

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email} {self.password}"
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Message(UserMixin, db.Model):
    __tablename__ = "message"
    message_id = db.Column(db.Integer, primary_key =True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    message_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.message_text