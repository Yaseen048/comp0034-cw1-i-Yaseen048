from flask import Flask


def create_app(config_class_name):
    """
    Initialise the Flask application.
    :type config_classname: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class_name)

    from flask_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
