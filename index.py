from pathlib import Path

from flask import Flask, jsonify, render_template

from db import execute, executescript, fetchone

dist = Path.joinpath(Path(__file__).parent, "front/dist")
app = Flask(__name__, static_folder=dist / "assets", template_folder=dist)

with open("schema.sql", "r") as f:
    executescript(f.read())


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/hw")
def api():
    return jsonify({"hello": "world"})


@app.route("/users")
def users():
    execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    return


if __name__ == "__main__":
    app.run(debug=True)
