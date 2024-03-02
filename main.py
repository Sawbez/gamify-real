from flask import Flask, render_template

app = Flask(__name__)
app.config['STATIC_FOLDER'] = "/front/dist/assets"
app.config['TEMPLATES_FOLDER'] = "/front/dist"

@app.route('/')
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)