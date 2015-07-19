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
    width = request.args.get('width', None)
    height = request.args.get('height', None)
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
    # return take_screenshot(url, dict(url=url, width=width, height=height, background=background))
    # return json.dumps(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route("/api")
def api_info():
    return render_template("api.html")

if __name__=='__main__':
    app.run(debug=True, port=5555)
