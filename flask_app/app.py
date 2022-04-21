from flask_app import create_app
from flask_app.config import DevelopmentConfig
from flask import render_template

app = create_app(DevelopmentConfig)


@app.route('/')

def index():
    return render_template('index.html', title="Home")


if __name__ == '__main__':
    app.run(debug=True)
