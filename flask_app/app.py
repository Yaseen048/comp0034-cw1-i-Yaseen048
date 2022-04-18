from flask_app import create_app
from flask_app.config import DevelopmentConfig

app = create_app(Config.DevelopmentConfig)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
