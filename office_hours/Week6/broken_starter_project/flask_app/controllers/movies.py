from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import director, movie

# This route will show all the movies from our database
@app.route("/movies")
def all_movies_page():
    return render_template("all_movies.html", all_movies = movie.Movie.grab_all_movies_with_directors())

# This route will display the NEW movie FORM (this is NOT the same as adding a movie to the database)
@app.route("/movies/new")
def new_movie_page():
    # Need to grab the directors for the dropdown in the HTML
    return render_template("add_movie.html", all_directors = director.Director.get_all_directors())

# Show the details about a specific movie from our database
@app.route("/movies/<int:id>/view") # Path variable called "id" that holds the ID of the individual movie
def view_movie_page(id):
    data = {
        "id": id,
    }
    return render_template("view_movie.html", this_movie = movie.Movie.grab_one_movie_with_director(data))

# Display the edit form for this specific movie
@app.route("/movies/<int:id>/edit") # Path variable called "id" that holds the ID of the individual movie
def edit_movie_page(id):
    data = {
        "id": id,
    }
    return render_template("edit_movie.html", this_movie = movie.Movie.grab_one_movie_with_director(data), all_directors = director.Director.get_all_directors())

## INVISIBLE ROUTES
# Delete a movie from our database
@app.route("/movies/<int:id>/delete")
def delete_movie(id):
    data = {
        "id": id,
    }
    movie.Movie.delete_movie(data)
    return redirect("/movies")

# Route to add a movie to the database (POST)
@app.route("/movies/add_to_db", methods=["POST"])
def add_movie_to_db():
    # Talk to the model to add this movie to the database
    data = {
        "title": request.form["title"],
        "genre": request.form["genre"],
        "release_date": request.form["release_date"],
        "box_office": request.form["box_office"],
        "director_id": request.form["director_id"], # IMPORTANT: Don't forget the foreign key!!!
    }
    movie.Movie.add_movie(data)
    # Once we're done, we need to redirect to a new route - ALWAYS redirect when you have POST routes
    return redirect("/movies")

# Route to edit a specific movie in the database (POST)
@app.route("/movies/<int:id>/edit_in_db", methods=["POST"]) # IMPORTANT: We need the ID because we need to know which movie we're editing
def edit_movie_in_db(id):
    data = {
        "title": request.form["title"],
        "genre": request.form["genre"],
        "release_date": request.form["release_date"],
        "box_office": request.form["box_office"],
        "director_id": request.form["director_id"], # IMPORTANT: Don't forget the foreign key!!!
        "id": id, # IMPORTANT: Don't forget the ID of the movie so we know which one we are editing!!!
    }
    movie.Movie.edit_movie(data)
    return redirect(f"/movies/{id}/view")