from flask_app import app
from flask import render_template, request, redirect, session # We'll import more here!
from flask_app.models import user # REMEMBER TO IMPORT YOUR MODELS!!
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument

# Define our routes here!!

@app.route("/")
def login_reg_page():
    return render_template("login_reg.html")

@app.route("/dashboard")
def dashboard_page():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("dashboard.html", this_user= user.User.get_user_by_id(data))

@app.route("/register", methods=["POST"])
def register_user():
    # Validate the registration first
    if not user.User.validate_registration(request.form):
        return redirect("/")
    # Save the newly registered user to the DB
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    session["user_id"] = user.User.register_user(data)
    # Redirect them appropriately
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def log_user_in():
    # We return the User object or False if the validations are no good
    found_user_or_false = user.User.validate_login(request.form)
    # Validate the registration first
    if not found_user_or_false:
        return redirect("/")
    # Get the correct user's id and save in session
    session["user_id"] = found_user_or_false.id
    # Redirect them appropriately
    return redirect("/dashboard")

@app.route('/logout')
def log_user_out():
    session.clear()
    return redirect('/')