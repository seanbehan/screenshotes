from flask import Flask, request
from library import take_and_save_screen_shot

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"


@app.route("/screenshot")
def screenshot():
    if request.args['url']:
        take_and_save_screen_shot(request.args['url'])

    return "Saved"
