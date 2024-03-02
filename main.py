from pathlib import Path

from flask import Flask, jsonify, render_template

dist = Path.joinpath(Path(__file__).parent, "front/dist")
app = Flask(__name__, static_folder=dist / "assets", template_folder=dist)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/hw")
def api():
    return jsonify({"hello": "world"})


if __name__ == "__main__":
    app.run(debug=True)
