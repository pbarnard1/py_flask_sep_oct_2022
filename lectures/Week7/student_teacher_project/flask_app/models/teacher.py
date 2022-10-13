from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # For validation messages
from flask_app.models import student

class Teacher:
    db_name = "students_teachers_schema" # CHANGE THIS TO MATCH YOUR SCHEMA NAME!  Class variable that holds the schema name

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.subject = data["subject"]
        self.is_tenured = data["is_tenured"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.students = [] # Hold a bunch of Students
        # We might need other attributes to hold additional values from your queries
        