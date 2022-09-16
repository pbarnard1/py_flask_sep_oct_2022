# The controllers will contain the routes for our project!
from flask_app import app
from flask import render_template

# Demo of various routes
@app.route('/hello')
def hello_page():
    return render_template("index.html")

# Path variable included
@app.route("/cities/<int:id>")
def city_page(id): # Remember the path variable here as a parameter!!
    return render_template("view_city.html", id = id) # Pass in value to HTML

@app.route("/cities")
def all_cities():
    # Placeholder for city data from the database
    all_cities = [
        {"id": 1, "name": "Seattle"},
        {"id": 2, "name": "Portland"},
    ]
    # Pass this list to the HTML
    return render_template("all_cities.html", all_cities = all_cities)