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
    return render_template("all_students.html", all_students = student.Student.get_all_students())

@app.route("/students/new")
def new_student_page():
    return render_template("add_student.html")

@app.route("/students/add_to_db", methods=["POST"])
def add_student_to_db():
    # Data dictionary
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "birthdate": request.form["birthdate"],
        "email": request.form["email"],
    }
    # Talk to the model to add a student
    student.Student.add_student(data)
    # Redirect somewhere
    return redirect("/students")

@app.route("/students/<int:id>/show")
def view_one_student_page(id):
    data = {
        "id": id
    }
    
    return render_template("view_student.html", 
        this_student = student.Student.grab_one_student_with_teachers(data),
        all_teachers_who_havent_taught_student = teacher.Teacher.get_teachers_who_have_not_taught_student(data))

# We'll also have a page to view each student - show each teacher and the class taught AND the semester as well, along with
# adding teachers to students and removing teachers from students

# We'll delete students
@app.route("/students/<int:id>/delete")
def remove_student_from_db(id):
    data = {
        "id": id
    }
    # Talk to model to remove student from DB
    student.Student.remove_student(data)
    # Redirect somewhere
    return redirect("/students")

@app.route("/students/<int:student_id>/add_teacher", methods=["POST"])
def add_teacher_to_student(student_id):
    data = {
        "semester": request.form["semester"],
        "student_id": student_id,
        "teacher_id": request.form["teacher_id"]
    }
    student.Student.add_teacher_to_student(data)
    return redirect(f"/students/{student_id}/show")

@app.route("/students/<int:student_id>/remove_teacher/<int:teacher_id>")
def remove_teacher_from_student(student_id, teacher_id):
    data = {
        "teacher_id": teacher_id,
        "student_id": student_id,
    }
    student.Student.remove_teacher_from_student(data)
    return redirect(f"/students/{student_id}/show")

