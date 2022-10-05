from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import director, movie


# Have the root route redirect to "/directors" route
@app.route("/")
def index():
    return redirect("/directors")

# This route will show all the directors from our database
@app.route("/directors")
def all_directors_page():
    # Don't forget to grab data from all the directors!
    return render_template("all_directors.html", all_directors = director.Director.get_all_directors())

# This route will display the NEW director FORM (this is NOT the same as adding a director to the database)
@app.route("/directors/new")
def new_director_page():
    return render_template("add_director.html") # Bug fix: File name in templates folder changed from "add_directors" to "add_director"

# Show the details about a specific director from our database
@app.route("/directors/<int:id>/view")
def view_director_page(id): # Bug fix: MUST pass in path variable as a parameter in your function definition
    data = {
        "id": id, # Bug fix: need data dictionary so we can grab one Director; notice "data" as an argument below
    }
    return render_template("view_director.html", this_director = director.Director.grab_one_director_with_all_movies(data))

@app.route("/directors/<int:id>/edit")
def edit_director_page(id):
    data = {
        "id": id,
    }
    return render_template("edit_director.html", this_director = director.Director.grab_one_director(data))


## INVISIBLE ROUTES
# Delete a director from our database
@app.route("/directors/<int:id>/delete")
def delete_director():
    director.Director.delete_director()
    return redirect("/directors")

# Route to add a director to the database (POST)
@app.route("/directors/add_to_db", methods=["POST"])
def add_director_to_db():
    # Bug fix: names in HTML must match the keys in request.form!
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "birth_date": request.form["birth_date"],
    }
    director.Director.add_director(data)
    return redirect("/directors")

# Route to edit a specific director in the database (POST)
@app.route("/directors/<int:id>/edit_in_db", methods=["POST"])
def edit_director_in_db():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "birthdate": request.form["birthdate"],
    }
    director.Director.edit_director(data)
    return redirect("/directors/<int:id>/view")
