from pathlib import Path

from flask import Flask, jsonify, render_template, send_from_directory
from jinja2 import TemplateError

from db import execute, executescript, fetchall, fetchone

dist = Path.joinpath(Path(__file__).parent, "front/dist")
app = Flask(__name__, static_folder=dist / "assets", template_folder=dist)

with open("schema.sql", "r") as f:
    execute(f.read())


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/hw")
def api():
    return jsonify({"hello": "world"})


@app.route("/users/<int:id_>")
def users(id_):
    execute("INSERT INTO Users (username) VALUES (%s)", (str(id_)))
    users = fetchall("SELECT * FROM Users")
    return jsonify({"data": users})


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def other(path):
    try:
        return render_template(f"index.html")
    except TemplateError:
        return 404


if __name__ == "__main__":
    app.run(debug=True)
