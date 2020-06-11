import os
from flask import Flask, redirect

app = Flask(__name__)

messages = []


def add_message(username, message):
    messages.append(f"{username}: {message}")


def get_all_messages():
    return "<br>".join(messages)


@app.route("/")
def index():
    return "<h1> Hello there </h2>"


@app.route("/<username>")
def user(username):
    return f"<h1>Welcome,{username}<h1/>{get_all_messages()}"


@app.route("/<username>/<message>")
def send_message(username, message):
    add_message(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
