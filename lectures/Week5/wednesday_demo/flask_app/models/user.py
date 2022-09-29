from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # For validation messages
#from flask_app.models import landmark # Next week, we'll import other models

class User:
    db_name = "landmarks_schema" # Class variable that holds the schema name
    # Add the init method when we tie in a real login/registration

    @staticmethod
    def validate_login(form_data):
        is_valid = True # Assume everything is good unless we find a problem
        # Perform our checks individually
        if len(form_data["user_name"]) < 2:
            flash("Name must be 2 or more characters")
            is_valid = False
        return is_valid

