from flask import Flask

app = Flask("__name__")

print("hello world")

@app.route("/")
def home():
    return "hellooooo"