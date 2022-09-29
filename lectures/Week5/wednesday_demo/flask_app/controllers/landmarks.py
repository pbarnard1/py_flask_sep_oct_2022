from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import landmark, city # NEW: import the model

# Display all landmarks with their cities linked
@app.route("/landmarks")
def all_landmarks_page():
    return render_template("all_landmarks.html", all_landmarks = landmark.Landmark.get_all_landmarks())

# Route that SHOWS the form for adding a landmark
@app.route("/landmarks/new")
def new_landmark_page():
    return render_template("add_landmark.html", all_cities = city.City.get_all_cities())

# Route to add landmark to the database
@app.route("/landmarks/add_to_db", methods=["POST"])
def add_landmark_to_db():
    if not landmark.Landmark.validate_landmark(request.form):
        return redirect("/landmarks/new")
    data = {
        "name": request.form["name"],
        "year_created": request.form["year_created"],
        "address": request.form["address"],
        "city_id": request.form["city_id"],
    }
    landmark.Landmark.add_landmark(data)
    return redirect("/landmarks")

@app.route("/landmarks/<int:id>/view")
def view_landmark_page(id):
    data = {
        "id": id
    }
    return render_template("show_landmark.html", this_landmark = landmark.Landmark.get_one_landmark(data))

@app.route("/landmarks/<int:id>/edit")
def edit_landmark_page(id):
    data = {
        "id": id
    }
    return render_template("edit_landmark.html", this_landmark = landmark.Landmark.get_one_landmark(data), all_cities = city.City.get_all_cities())

# Route that edits the landmark in the database
@app.route("/landmarks/<int:id>/edit_in_db", methods=["POST"])
def edit_landmark_in_db(id):
    if not landmark.Landmark.validate_landmark(request.form):
        return redirect(f"/landmarks/{id}/edit")
    data = {
        "name": request.form["name"],
        "year_created": request.form["year_created"],
        "address": request.form["address"],
        "city_id": request.form["city_id"],
        "id": id, # VERY IMPORTANT: Need the ID so we know which landmark we're editing
    }
    # Talk to model to edit landmark in DB
    landmark.Landmark.edit_landmark(data)
    return redirect(f"/landmarks/{id}/view") # Need an f-string to put the ID in

@app.route("/landmarks/<int:id>/delete")
def delete_landmark(id):
    data = {
        "id": id,
    }
    landmark.Landmark.delete_landmark(data)
    return redirect("/landmarks")
