from flask_app import app
from flask import render_template, request, redirect, session

# Show the login page
@app.route("/")
def login_reg_page():
    return render_template("home_page.html")

# This will "log in" the user
@app.route("/login", methods=["POST"])
def login():
    session["user_name"] = request.form["user_name"]
    return redirect("/cities")

@app.route('/logout')
def logout():
    session.clear() # Deletes session
    return redirect("/") # Send back to log-in/reg page