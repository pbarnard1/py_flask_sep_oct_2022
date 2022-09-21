from flask_ap import app
from flask import render_template
@app.route("/")
def all_games_page():
    my_games = [
        {
            "id": 1,
            "name": "Monopoly",
            "rating": 4.8,
            "first_name": "Adrian",
            "last_name": "Barnard"
        },
        {
            "id": 2,
            "name": "Hearts",
            "rating": 3.8,
            "first_name": "Jenny",
            "last_name": "Rocket"
        },
        {
            "id": 3,
            "name": "Xenoblade Chronicles",
            "rating": 4.2,
            "first_name": "Shulk",
            "last_name": "Hogan"
        },
        {
            "id": 4,
            "name": "Tic-Tac-Doe",
            "rating": 2.7,
            "first_name": "Adrian",
            "last_name": "Barnard"
        },
    ]
    return render_template("all_game.html", my_games = my_games)

@app.route("/games/new")
def add_game_page():
    return render_template("new_game.html")

@app.route("/games/add_to_db")
def add_game_to_db():
    # Placeholder for adding to db goes here
    
    # Interim fix: put form data in session
    session["game"] = request.form["game"]
    session["rating"] = request.form["rating"]
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    return redirect("/game_added")

@app.route("/game_added")
def show_game_from_form():
    return render_template("game_from_form.html")
