from pathlib import Path
from typing import *
from typing import Optional

from flask import Flask, jsonify, render_template, request, session
from flask_session import Session
from jinja2 import TemplateError

from db import execute, fetchall, fetchone
from schema import *

dist = Path.joinpath(Path(__file__).parent, "front/dist")
app = Flask(__name__, static_folder=str(dist / "assets"), template_folder=str(dist))
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


with open("schema.sql", "r") as f:
    execute(f.read())


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/hw")
def api():
    return jsonify({"hello": "world"})

@app.route("/users/<string:username>", methods=["GET", "POST"])
@app.route("/users/", methods=["GET"])
def users(username: Optional[str] = None):
    if request.method == "GET":
        if username:
            user = fetchone("SELECT * FROM Users WHERE username = %s", (username,), dtype=User)
            if (user):
                #success
                session["username"] = user.username
                return jsonify(user)
            else:
                # failure
                return jsonify({"result": "failure"}), 404

        else:
            users = fetchall("SELECT * FROM Users", dtype=User)
            return jsonify(users)
    elif request.method == "POST":
        execute("INSERT INTO Users (username) VALUES (%s)", (username,))
        return jsonify({ "message": "success" })
    else:
        return 404

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def other(path):
    try:
        return render_template("index.html", session=session)
    except TemplateError:
        return "404", 404


if __name__ == "__main__":
    app.run(debug=True)
