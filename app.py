from flask import Flask, render_template

app = Flask("__name__")

print("hello world")

# @app.route("/")
# def home():
#     return "hellooooo"

@app.route("/")
def setup():
    return render_template('index.html')