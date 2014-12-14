from flask import Flask, request
from library import take_screenshot

app = Flask(__name__)
# app.config['DEBUG'] = True


@app.route("/")
def index():
    return "Hello World"


@app.route("/screenshot")
def screenshot():
    if request.args['url']:
        take_screenshot(request.args['url'])

    return "Saved"
