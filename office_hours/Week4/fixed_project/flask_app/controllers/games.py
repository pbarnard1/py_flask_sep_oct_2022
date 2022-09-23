from flask_app import app # Bug fix: flask_app, NOT flask_ap
from flask import render_template, request, session, redirect
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
    # Bug fix: all_games.html - must match file names exactly, otherwise you get a TemplateNotFound error
    # Bug fix: folder name must be "templates" - NOT "template"
    # Bug fix: need {% endfor %} in HTML
    # Bug fix: {{ }} {{ }} for displaying the name
    # Bug fix: all_games = ..., NOT my_games = ..., so we match the HTML variable name
    # Bug fix: game["name"], NOT game["game"]
    return render_template("all_games.html", all_games = my_games)

@app.route("/games/new")
def add_game_page():
    return render_template("new_game.html")

# Bug fix: needed to import request, session and redirect
# Bug fix: need methods=["POST"] for POST requests
# Bug fix: Need name='' for any fields where you are entering value
@app.route("/games/add_to_db", methods=["POST"])
def add_game_to_db():
    # Placeholder for adding to db goes here (future)
    
    # Interim fix: put form data in session
    session["name"] = request.form["name"] # Bug fix: "name", not "game"
    session["rating"] = request.form["rating"]
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    return redirect("/game_added")

@app.route("/game_added")
def show_game_from_form():
    # Bug fixes: file name must match;
    # Also need to use {{ }} {{ }} for displaying the name
    return render_template("game_from_form.html")
