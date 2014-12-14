import os
import json
from flask import Flask, request, render_template
from library import take_screenshot, getenv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/screenshot")
def screenshot():
    url = str(request.args['url'])
    if "fullpagescreenshots" in url:
        return "Sorry, not allowed", 405

    data = {}
    if request.args['url']:
        data = take_screenshot(url)

    return json.dumps(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

if getenv()=="development":
    if __name__ == "__main__":
        app.run(debug=True)
