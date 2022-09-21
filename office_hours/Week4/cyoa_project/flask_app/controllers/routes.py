from flask_app import app
from flask import render_template

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/look")
def look_around():
    return render_template("look.html")

@app.route("/sleep")
def sleep():
    return render_template("sleep.html")