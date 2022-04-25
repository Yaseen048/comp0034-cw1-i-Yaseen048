from flask import Flask
from dash import Dash
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import dash_bootstrap_components as dbc
from flask.helpers import get_root_path

csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()
csrf._exempt_views.add("dash.dash.dispatch")

def create_app(config_class_name):
    """
    Initialise the Flask application.
    :type config_classname: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class_name)
    register_dashapp(app)

    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        from flask_app.models import User
        db.create_all()

    
    from flask_app.main.routes import main_bp
    app.register_blueprint(main_bp)

    from flask_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from flask_app.chat.routes import chat_bp
    app.register_blueprint(chat_bp)

    return app

def register_dashapp(app):
    from flask_app.cinema_dash_app import layout
    from flask_app.cinema_dash_app.callbacks import register_callbacks

    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp = Dash(__name__,
                    server=app,
                    url_base_pathname='/dashboard/',
                    assets_folder=get_root_path(__name__) + '/dashboard/assets/',
                    meta_tags=[meta_viewport],
                    external_stylesheets=[dbc.themes.SKETCHY])

    with app.app_context():
        dashapp.title = 'Dashboard'
        dashapp.layout = layout.layout
        register_callbacks(dashapp)