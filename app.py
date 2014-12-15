import os, json
from flask import Flask, request, render_template
from library import take_screenshot

app = Flask(__name__)
app.debug = os.environ.get("DEBUG")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/screenshot")
def screenshot():
    url = str(request.args['url'])
    if "screenshot.es" in url:
        return "Sorry, not allowed", 405

    data = {}
    if request.args['url']:
        data = take_screenshot(url)

    return json.dumps(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route("/api")
def api_info():
    return render_template("api.html")
