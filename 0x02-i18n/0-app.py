from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''Index page of the application'''
    return render_template('0-index.html')


if __name__ == '__main__':
    '''Main application'''
    app.run(debug=True)
