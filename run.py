import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Hello there </h2>"


@app.route("/<username>")
def user(username):
    return "Hi " + username


@app.route("/<username>/<message>")
def send_message(username, message):
    return f"{username}: {message}"


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
