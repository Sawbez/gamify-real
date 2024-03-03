from pathlib import Path
from typing import Optional

from flask import Flask, jsonify, render_template, send_from_directory, request
from jinja2 import TemplateError

from db import execute, fetchall, fetchone
from typing import List, TypedDict

class Category(TypedDict):
    id: int
    name: str

class Achievement(TypedDict):
    id: int
    name: str
    description: str
    points: int
    categoryId: int

class User(TypedDict):
    id: int
    username: str

class UserExperience(TypedDict):
    userId: int
    categoryId: int
    experience: int

class UserLevel(TypedDict):
    userId: int
    categoryId: int
    level: int

class UserAchievement(TypedDict):
    userId: int
    achievementId: int

class Task(TypedDict):
    id: int
    userId: int
    name: str
    description: str
    points: int
    categoryId: int

class SubTask(TypedDict):
    id: int
    taskId: int
    name: str
    description: str
    points: int

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

@app.route("/users/<string:username>", methods=["GET", "POST"])
def users(username: Optional[str] = None):
    if request.method == "GET":
        if username:
            user = fetchone("SELECT * FROM Users WHERE username = %s", (username,))
            if (user):
                #success
                return jsonify({
                    "username": user[1],
                    "id": user[0],
                })
            else:
                # failure
                return jsonify({"result": "failure"}), 404

        else:
            users = fetchall("SELECT * FROM Users")
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
        return render_template(f"index.html")
    except TemplateError:
        return 404


if __name__ == "__main__":
    app.run(debug=True)
