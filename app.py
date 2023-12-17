from flask import Flask, render_template

app = Flask("__name__")

print("hello world")

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/setup")
def setup():
    return render_template('setup.html')