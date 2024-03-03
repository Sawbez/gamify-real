from pathlib import Path

from flask import Flask, jsonify, render_template, send_from_directory

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


@app.route("/users/<int:id>")
def users():
    execute("INSERT INTO Users (name) VALUES (%s)", ("abacadaba"))
    users = fetchall()
    return jsonify(users)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')



if __name__ == "__main__":
    app.run(debug=True)
