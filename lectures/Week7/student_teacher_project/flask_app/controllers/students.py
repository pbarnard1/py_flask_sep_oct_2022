from flask import render_template, redirect, request, session
from flask_app import app
# IMPORT THE FILE - DO NOT IMPORT THE MODEL DIRECTLY!!  Otherwise you run into circular imports!
from flask_app.models import student, teacher

@app.route("/")
def main_route():
    return redirect('/students')

# All students page
@app.route('/students')
def all_students_page():
    pass

@app.route("/students/new")
def new_student_page():
    return render_template("add_student.html")

@app.route("/students/add_to_db", methods=["POST"])
def add_student_to_db():
    pass

# We'll also have a page to view each student - show each teacher and the class taught AND the semester as well, along with
# adding teachers to students and removing teachers from students

# We'll delete students

