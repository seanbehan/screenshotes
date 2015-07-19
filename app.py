import os, json
from flask import Flask, request, render_template, jsonify
from library import take_screenshot

app = Flask(__name__)
app.debug = os.environ.get("DEBUG")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/screenshot")
def screenshot():
    url = request.args.get('url', None)
    width = request.args.get('width', 1200)
    height = request.args.get('height', 750)
    background = request.args.get('background', None)

    opts = dict(
        url=url,
        width=width,
        height=height,
        background=background
    )

    if "screenshot.es" in url:
        return jsonify(dict(message="Sorry, not allowed", code=405))

    return jsonify(
        take_screenshot(opts)
    )

@app.route("/api")
def api_info():
    return render_template("api.html")

if __name__=='__main__':
    app.run(debug=True, port=5555)
