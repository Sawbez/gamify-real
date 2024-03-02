from pathlib import Path

from flask import Flask, jsonify, render_template

from db import execute, executescript, fetchall, fetchone

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


@app.route("/users/<int:id>")
def users():
    execute("INSERT INTO Users (name) VALUES (%s)", ("abacadaba"))
    users = fetchall()
    return jsonify(users)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path


if __name__ == "__main__":
    app.run(debug=True)
