import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"

now = datetime.now().strftime("%H:%H:%S")
messages = []


def add_message(username, message):
    message_dict = {"time": now, "username": username, "message": message}
    messages.append(message_dict)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(session["username"])
    return render_template("index.html")


@app.route("/<username>", methods=["GET", "POST"])
def user(username):
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(session["username"])
    else:
        return render_template("chat.html", username=username,
                               chat_messages=messages)


@app.route("/<username>/<message>")
def send_message(username, message):
    add_message(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
