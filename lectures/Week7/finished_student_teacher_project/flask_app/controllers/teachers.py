from flask import render_template, redirect, request, session
from flask_app import app
# IMPORT THE FILE - DO NOT IMPORT THE MODEL DIRECTLY!!  Otherwise you run into circular imports!
from flask_app.models import student, teacher

# All teachers page
@app.route('/teachers')
def all_teachers_page():
    return render_template("all_teachers.html", all_teachers = teacher.Teacher.get_all_teachers())

@app.route("/teachers/new")
def new_teacher_page():
    return render_template("add_teacher.html")

@app.route("/teachers/add_to_db", methods=["POST"])
def add_teacher_to_db():
    # Data dictionary
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "subject": request.form["subject"],
        "is_tenured": request.form["is_tenured"],
        "email": request.form["email"],
    }
    # Talk to the model to add a teacher
    teacher.Teacher.add_teacher(data)
    # Redirect somewhere
    return redirect("/teachers")

@app.route("/teachers/<int:id>/show")
def view_one_teacher_page(id):
    data = {
        "id": id
    }
    
    return render_template("view_teacher.html", 
        this_teacher = teacher.Teacher.grab_one_teacher_with_students(data),
        all_students_not_taught_by_teacher = student.Student.get_students_not_taught_by_teacher(data))

# We'll delete teachers
@app.route("/teachers/<int:id>/delete")
def remove_teacher_from_db(id):
    data = {
        "id": id
    }
    # Talk to model to remove teacher from DB
    teacher.Teacher.remove_teacher(data)
    # Redirect somewhere
    return redirect("/teachers")

@app.route("/teachers/<int:teacher_id>/add_student", methods=["POST"])
def add_student_to_teacher(teacher_id):
    data = {
        "semester": request.form["semester"],
        "teacher_id": teacher_id,
        "student_id": request.form["student_id"]
    }
    student.Student.add_teacher_to_student(data)
    return redirect(f"/teachers/{teacher_id}/show")

@app.route("/teachers/<int:teacher_id>/remove_student/<int:student_id>")
def remove_student_from_teacher(teacher_id, student_id):
    data = {
        "teacher_id": teacher_id,
        "student_id": student_id,
    }
    student.Student.remove_teacher_from_student(data)
    return redirect(f"/teachers/{teacher_id}/show")

