from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

csrf = CSRFProtect()
db = SQLAlchemy()
Login_manager = LoginManager()

def create_app(config_class_name):
    """
    Initialise the Flask application.
    :type config_classname: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class_name)
    csrf.init_app(app)
    db.init_app(app)
    Login_manager.init_app(app)
    Login_manager.login_view = 'auth.login'

    with app.app_context():
        from flask_app.models import User
        db.create_all()

    
    from flask_app.main.routes import main_bp
    app.register_blueprint(main_bp)

    from flask_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
