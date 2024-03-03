from pathlib import Path
from typing import Optional

from flask import Flask, jsonify, render_template, send_from_directory, request,session
from flask_session import Session
from jinja2 import TemplateError


from db import execute, fetchall, fetchone
from typing import *
from schema import *

dist = Path.joinpath(Path(__file__).parent, "front/dist")
app = Flask(__name__, static_folder=dist / "assets", template_folder=dist)
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
            user = fetchone("SELECT * FROM Users WHERE username = %s", (username,))
            if (user):
                #success
                session["username"] = user[1]
                return jsonify({
                    "username": user[1],
                    "id": user[0],
                })
            else:
                # failure
                return jsonify({"result": "failure"}), 404

        else:
            users = fetchall("SELECT * FROM Users", data_class=User)
            print(users)
            usersobj = []
            for user in users:
                usersobj.append ({
                    "username": user[1],
                    "id": user[0],
                })
            return jsonify(usersobj)
    elif request.method == "POST":
        execute("INSERT INTO Users (username) VALUES (%s)", (username,))
        return jsonify({ "message": "success" })
    else:
        return 404


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def other(path):
    try:
        return render_template(f"index.html", session=session)
    except TemplateError:
        return "404", 404


if __name__ == "__main__":
    app.run(debug=True)
