#!/usr/bin/env python3
'''Module creates an i18n app'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''Babel's Config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''Get locale for app'''
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    '''Index page of the application'''
    return render_template('2-index.html')


if __name__ == '__main__':
    '''Main application'''
    app.run(debug=True)
