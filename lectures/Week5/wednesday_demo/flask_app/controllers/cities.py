from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import city # NEW: import the model

@app.route("/cities/new")
def new_city_form():
    return render_template("new_city.html")

@app.route("/cities/add_to_db", methods=["POST"])
def add_city_to_db():
    print("Before redirecting:")
    print(request.form) # Print the mayor of the city from the form
    if not city.City.validate_city(request.form):
        return redirect(f"/cities/new")
    # Data dictionary that we'll use to add the city to the database
    data = {
        "name": request.form["name"],
        "mayor": request.form["mayor"],
        "population": request.form["population"]
    }
    # Talk to model to add city to DB
    city.City.create_city(data)
    return redirect("/cities")

# Renamed route - route to show one city
@app.route("/cities/<int:id>/show")
def show_city(id):
    data = {
        "id": id
    }
    return render_template("show_city.html", this_city = city.City.get_one_city_with_landmarks(data))

# Show all cities from the database
@app.route("/cities")
def all_cities_page():
    # Show all cities (in a bit)
    return render_template("all_cities.html", all_cities = city.City.get_all_cities())

# Edit page route (NOT the same as editing in the database)
@app.route("/cities/<int:id>/edit")
def edit_city_page(id):
    data = {
        "id": id
    }
    return render_template("edit_city.html", this_city = city.City.get_one_city(data))

# Route that edits the city in the database
@app.route("/cities/<int:id>/edit_in_db", methods=["POST"])
def edit_city_in_db(id):
    if not city.City.validate_city(request.form):
        return redirect(f"/cities/{id}/edit")
    data = {
        "name": request.form["name"],
        "mayor": request.form["mayor"],
        "population": request.form["population"],
        "id": id, # VERY IMPORTANT: Need the ID so we know which city we're editing
    }
    # Talk to model to add city to DB
    city.City.edit_city(data)
    return redirect(f"/cities/{id}/show") # Need an f-string to put the ID in

# Route that deletes a city from the database
@app.route("/cities/<int:id>/delete")
def delete_city(id):
    data = {
        "id": id,
    }
    city.City.delete_city(data)
    return redirect("/cities")
