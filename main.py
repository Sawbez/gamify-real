from pathlib import Path

from flask import Flask, render_template

dist = Path.joinpath(Path(__file__).parent, "front/dist")
app = Flask(__name__, static_folder=dist / "assets", template_folder=dist)


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
