from pathlib import Path
from typing import *
from typing import Optional
from flask_cors import CORS

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
CORS(app)

with open("schema.sql", "r") as f:
    execute(f.read())


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/hw")
def api():
    return jsonify({"hello": "world"})

#region Low-level API

def category_to_id(category: str) -> int:
    return fetchone("SELECT id FROM Categories WHERE name = %s", (category,))[0]

@app.route("/users", methods=["GET"])
@app.route("/users/<string:username>", methods=["GET", "POST"])
def users(username: Optional[str] = None):
    if request.method == "GET":
        if username:
            user = fetchone("SELECT * FROM Users WHERE username = %s", (username,), dtype=User)
            if (user):
                session["username"] = user.username
                return jsonify(user)
            else:
                return jsonify({ "result": "failure" })

        else:
            users = fetchall("SELECT * FROM Users", dtype=User)
            return jsonify(users)
    elif request.method == "POST":
        execute("INSERT INTO Users (username) VALUES (%s)", (username,))
        session["username"] = username
        return jsonify({ "message": "success" })
    else:
        return 404

@app.route("/categories", methods=["GET", "POST"])
def categories():
    if request.method == "GET":
        categories = fetchall("SELECT * FROM Categories", dtype=Category)
        return jsonify(categories)
    elif request.method == "POST":
        data: Category = request.get_json()
        #clear the screen for debug
        execute("INSERT INTO Categories (name) VALUES (%s)", (data["name"],))
        return jsonify({ "message": "success" })
    else:
        return 404

@app.route("/achievements", methods=["GET"])
@app.route("/achievements/<int:category_id>", methods=["GET"]) # Get achievements by category
@app.route("/achievements/<int:achievement_id>", methods=["GET", "POST"]) # Get achievement by id
def achievements(category_id: Optional[int] = None, achievement_id: Optional[int] = None):
    if category_id:
        #probably should be a join
        achievements = fetchall("SELECT * FROM Achievements WHERE categoryId = %s", (category_id,), dtype=Achievement)
        return jsonify(achievements)
    elif achievement_id:
        if request.method == "GET":
            achievement = fetchone("SELECT * FROM Achievements WHERE id = %s", (achievement_id,), dtype=Achievement)
            return jsonify(achievement)
        elif request.method == "POST":
            data: Achievement = request.get_json()
            execute("INSERT INTO Achievments (name, description, points, categoryId) VALUES (%s, %s, %s, %s)", (data["name"], data["description"], data["points"], data["categoryId"]))
            return jsonify({ "message": "success" })
    else:
        achievements = fetchall("SELECT * FROM Achievements", dtype=Achievement)
        return jsonify(achievements)

@app.route("/users/experience/<int:user_id>", methods=["GET"])
@app.route("/users/experience/<int:user_id>/<int:category_id>", methods=["GET", "POST", "PUT"])
def user_experience(user_id: int, category_id: Optional[int] = None):
    if request.method == "GET":
        if category_id:
            user_experience = fetchone("SELECT * FROM UserExperience WHERE userId = %s AND categoryId = %s", (user_id, category_id), dtype=UserExperience)
            return jsonify(user_experience)
        else:
            user_experience = fetchall("SELECT * FROM UserExperience WHERE userId = %s", (user_id,), dtype=UserExperience)
            return jsonify(user_experience)
    elif request.method == "POST":
        data: UserExperience = request.get_json()
        execute("INSERT INTO UserExperience (userId, categoryId, experience) VALUES (%s, %s, %s)", (data["userId"], data["categoryId"], data["experience"]))
        return jsonify({ "message": "success" })
    elif request.method == "PUT":
        data: UserExperience = request.get_json()
        execute("UPDATE UserExperience SET experience = %s WHERE userId = %s AND categoryId = %s", (data["experience"], data["userId"], data["categoryId"]))
        return jsonify({ "message": "success" })
    else:
        return 404

@app.route("/users/level/<int:user_id>", methods=["GET"])
@app.route("/users/level/<int:user_id>/<int:category_id>", methods=["GET", "POST", "PUT"])
def user_level(user_id: int, category_id: Optional[int] = None):
    if request.method == "GET":
        if category_id:
            user_level = fetchone("SELECT * FROM UserLevel WHERE userId = %s AND categoryId = %s", (user_id, category_id), dtype=UserLevel)
            return jsonify(user_level)
        else:
            user_level = fetchall("SELECT * FROM UserLevel WHERE userId = %s", (user_id,), dtype=UserLevel)
            return jsonify(user_level)
    elif request.method == "POST":
        data: UserLevel = request.get_json()
        execute("INSERT INTO UserLevel (userId, categoryId, level) VALUES (%s, %s, %s)", (data["userId"], data["categoryId"], data["level"]))
        return jsonify({ "message": "success" })
    elif request.method == "PUT":
        data: UserLevel = request.get_json()
        execute("UPDATE UserLevel SET level = %s WHERE userId = %s AND categoryId = %s", (data["level"], data["userId"], data["categoryId"]))
        return jsonify({ "message": "success" })
    else:
        return 404

@app.route("/users/achievements/<int:user_id>", methods=["GET"])
@app.route("/users/achievements/<int:user_id>/<int:achievement_id>", methods=["GET", "POST"])
def user_achievements(user_id: int, achievement_id: Optional[int] = None):
    if request.method == "GET":
        if achievement_id:
            user_achievement = fetchone("SELECT * FROM UserAchievements WHERE userId = %s AND achievementId = %s", (user_id, achievement_id), dtype=UserAchievement)
            return jsonify(user_achievement)
        else:
            user_achievements = fetchall("SELECT * FROM UserAchievements WHERE userId = %s", (user_id,), dtype=UserAchievement)
            return jsonify(user_achievements)
    elif request.method == "POST":
        data: UserAchievement = request.get_json()
        execute("INSERT INTO UserAchievements (userId, achievementId) VALUES (%s, %s)", (data["userId"], data["achievementId"]))
        return jsonify({ "message": "success" })
    else:
        return 404

@app.route("/tasks", methods=["GET"])
@app.route("/tasks/<int:user_id>", methods=["GET", "POST"])
@app.route("/tasks/<int:user_id>/<int:task_id>", methods=["GET", "POST", "PUT"])
@app.route("/tasks/<int:user_id>/<int:task_id>/subtasks", methods=["GET", "POST"])
@app.route("/tasks/<int:user_id>/<int:task_id>/subtasks/<int:subtask_id>", methods=["GET", "POST", "PUT"])
def tasks(user_id: Optional[int] = None, task_id: Optional[int] = None, subtask_id: Optional[int] = None):
    if request.method == "GET":
        if user_id:
            if task_id:
                if subtask_id:
                    subtask = fetchone("SELECT * FROM SubTasks WHERE id = %s", (subtask_id,), dtype=SubTask)
                    return jsonify(subtask)
                else:
                    subtasks = fetchall("SELECT * FROM SubTasks WHERE taskId = %s", (task_id,), dtype=SubTask)
                    return jsonify(subtasks)
            else:
                tasks = fetchall("SELECT * FROM Tasks WHERE userId = %s", (user_id,), dtype=Task)
                return jsonify(tasks)
        else:
            tasks = fetchall("SELECT * FROM Tasks", dtype=Task)
            return jsonify(tasks)
    elif request.method == "POST":
        if task_id:
            data: SubTask = request.get_json()
            execute("INSERT INTO SubTasks (taskId, name, description, points) VALUES (%s, %s, %s, %s)", (data["taskId"], data["name"], data["description"], data["points"]))
            return jsonify({ "message": "success" })
        else:
            data: Task = request.get_json()
            execute("INSERT INTO Tasks (userId, name, description, points, categoryId) VALUES (%s, %s, %s, %s, %s)", (data["userId"], data["name"], data["description"], data["points"], data["categoryId"]))
            return jsonify({ "message": "success" })
    elif request.method == "PUT":
        if task_id:
            data: SubTask = request.get_json()
            execute("UPDATE SubTasks SET name = %s, description = %s, points = %s WHERE id = %s", (data["name"], data["description"], data["points"], subtask_id))
            return jsonify({ "message": "success" })
        else:
            data: Task = request.get_json()
            execute("UPDATE Tasks SET name = %s, description = %s, points = %s, categoryId = %s WHERE id = %s", (data["name"], data["description"], data["points"], data["categoryId"], task_id))
            return jsonify({ "message": "success" })
    else:
        return 404
#endregion

#region High-level API
@app.route("/users/<string:username>/achievements", methods=["GET, POST"])
def hl_user_achievements(username: str):
    user = fetchone("SELECT * FROM Users WHERE username = %s", (username,), dtype=User)
    if not user:
        return jsonify({ "result": "failure" }), 404

    if request.method == "GET":
        achievements = fetchall("SELECT * FROM UserAchievements WHERE userId = %s", (user.id,), dtype=UserAchievement)
        return jsonify(achievements)
    elif request.method == "POST":
        data: UserAchievement = request.get_json()
        execute("INSERT INTO UserAchievements (userId, achievementId) VALUES (%s, %s)", (user.id, data["achievementId"]))
        return jsonify({ "message": "success" })

class TaskWithSubtasks(Task):
    subtasks: List[SubTask]

@app.route("/users/<string:username>/tasks", methods=["GET", "POST"])
@app.route("/users/<string:username>/tasks/<int:task_id>", methods=["GET", "POST", "DELETE"])
def hl_user_tasks(username: str, task_id: Optional[int] = None):
    user = fetchone("SELECT * FROM Users WHERE username = %s", (username,), dtype=User)
    if not user:
        return jsonify({ "result": "failure" }), 404

    if request.method == "GET":
        if task_id:
            task = fetchone("SELECT * FROM Tasks WHERE id = %s", (task_id,), dtype=Task)
            subtasks = fetchall("SELECT * FROM SubTasks WHERE taskId = %s", (task_id,), dtype=SubTask)
            task.subtasks = subtasks
            return jsonify(task)
        tasks = fetchall("SELECT * FROM Tasks WHERE userId = %s", (user.id,), dtype=Task)
        return jsonify(tasks)
    elif request.method == "POST":
        if task_id:
            data: SubTask = request.get_json()
            execute("INSERT INTO SubTasks (taskId, name, description, points) VALUES (%s, %s, %s, %s)", (task_id, data["name"], data["description"], data["points"]))
            return jsonify({ "message": "success" })
        data: TaskWithSubtasks = request.get_json()
        execute("INSERT INTO Tasks (userId, name, description, points, categoryId) VALUES (%s, %s, %s, %s, %s)", (user.id, data["name"], data["description"], data["points"], data["categoryId"]))
        '''
        if data["subtasks"]:
            task = fetchone("SELECT * FROM Tasks WHERE userId = %s AND name = %s", (user.id, data["name"]), dtype=Task)
            for subtask in data["subtasks"]:
                execute("INSERT INTO SubTasks (taskId, name, description, points) VALUES (%s, %s, %s, %s)", (task.id, subtask.name, subtask.description, subtask.points))
        '''
        return jsonify({ "message": "success" })
        
    elif request.method == "DELETE":
        #get the experience number of the task
        task = fetchone("SELECT * FROM Tasks WHERE id = %s", (task_id,), dtype=Task)
        #delete the task
        execute("DELETE FROM Tasks WHERE id = %s", (task_id,))
        #add the experience back to the user
        execute("UPDATE UserExperience SET experience = experience - %s WHERE userId = %s AND categoryId = %s", (task.points, user.id, task.categoryId))
        return jsonify({ "message": "success" })
    else:
        return 404

@app.route("/users/<string:username>/experience", methods=["GET", "PATCH"])
def hl_user_experience(username: str):
    user = fetchone("SELECT * FROM Users WHERE username = %s", (username,), dtype=User)
    if not user:
        return jsonify({ "result": "failure" }), 404

    if request.method == "GET":
        user_experience = fetchall("SELECT * FROM UserExperience WHERE userId = %s", (user.id,), dtype=UserExperience)
        return jsonify(user_experience)
    elif request.method == "PATCH":
        data: UserExperience = request.get_json()
        execute("UPDATE UserExperience SET experience = %s WHERE userId = %s AND categoryId = %s", (data["experience"], user.id, data["categoryId"]))
        return jsonify({ "message": "success" })
    else:
        return 404

@app.route("/users/<string:username>/level", methods=["GET", "PATCH"])
def hl_user_level(username: str):
    user = fetchone("SELECT * FROM Users WHERE username = %s", (username,), dtype=User)
    if not user:
        return jsonify({ "result": "failure" }), 404

    if request.method == "GET":
        user_level = fetchall("SELECT * FROM UserLevel WHERE userId = %s", (user.id,), dtype=UserLevel)
        return jsonify(user_level)
    elif request.method == "PATCH":
        data: UserLevel = request.get_json()
        execute("UPDATE UserLevel SET level = %s WHERE userId = %s AND categoryId = %s", (data["level"], user.id, data["categoryId"]))
        return jsonify({ "message": "success" })
    else:
        return 404

#endregion

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def other(path):
    try:
        # return render_template("index.html", session=session)
        return jsonify({ "result": "failure" }), 404
    except TemplateError:
        return "404", 404


if __name__ == "__main__":
    app.run(debug=True)
