from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # For validation messages
# We'll be importing additional stuff here!

class User:
    db_name = "landmarks_schema" # CHANGE THIS TO MATCH YOUR SCHEMA NAME!  Class variable that holds the schema name
    
    def __init__(self, data):
        pass # We'll fill this in

    # Add methods to create a new user and perhaps more!


    # Validation login and registration here!