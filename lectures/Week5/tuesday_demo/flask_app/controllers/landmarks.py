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
    data = {
        "name": request.form["name"],
        "year_created": request.form["year_created"],
        "address": request.form["address"],
        "city_id": request.form["city_id"],
    }
    landmark.Landmark.add_landmark(data)
    return redirect("/landmarks")