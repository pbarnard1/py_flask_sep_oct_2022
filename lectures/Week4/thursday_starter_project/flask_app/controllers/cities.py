from flask_app import app
from flask import render_template, request, redirect, session

@app.route("/cities/new")
def new_city_form():
    return render_template("new_city.html")

@app.route("/cities/add_to_db", methods=["POST"])
def add_city_to_db():
    print("Before redirecting:")
    print(request.form) # Print the mayor of the city from the form
    # Save the data from the form into session - FOR NOW
    session["mayor"] = request.form["mayor"]
    session["name"] = request.form["name"]
    session["population"] = request.form["population"]
    # We'll later on add the data properly to the database
    # and not use session for this
    return redirect("/cities/show_city")

@app.route("/cities/show_city")
def show_city():
    print("After redirecting:")
    print(request.form)
    # No need to send session data through render template
    return render_template("show_city.html")