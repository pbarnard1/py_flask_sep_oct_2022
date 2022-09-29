from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import landmark # Next week, we'll import other models
from flask import flash

class City:
    db_name = "landmarks_schema" # Class variable that holds the schema name

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.mayor = data["mayor"]
        self.population = data["population"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # Add a new attribute in week 5: landmarks
        self.landmarks = [] # Link MULTIPLE Landmarks to this City

    # Class method will contain your queries
    @classmethod
    def create_city(cls, data):
        query = """
        INSERT INTO cities
        (name, mayor, population)
        VALUES (%(name)s, %(mayor)s, %(population)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Grab all cities
    @classmethod
    def get_all_cities(cls):
        query = "SELECT * FROM cities;"
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        all_city_objects = [] # List of City objects
        # Take each city and turn it into an object
        if len(results) == 0: # If no cities found, return an empty list
            return []
        else: # At least one city found
            for this_city_dictionary in results:
                print(this_city_dictionary)
                # Create the City object
                this_city_obj = cls(this_city_dictionary)
                # Add this City object to the list
                all_city_objects.append(this_city_obj)
            return all_city_objects

    # Grab one city
    @classmethod
    def get_one_city(cls, data):
        query = "SELECT * FROM cities WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0: # If no cities found, return an empty list
            return None
        else: # city found
            return cls(results[0]) # Create object and return it

    @classmethod
    def get_one_city_with_landmarks(cls, data):
        query = """
        SELECT * FROM cities 
        LEFT JOIN landmarks 
        ON landmarks.city_id = cities.id 
        WHERE cities.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0: # If no cities found, return an empty item (None)
            return None
        else: # city found
            # Create the city object
            this_city_object = cls(results[0])
            # For each landmark, we'll need to:
            for this_landmark in results:
                # Grab the landmark's information
                new_landmark_dictionary = {
                    "id": this_landmark["landmarks.id"],
                    "name": this_landmark["landmarks.name"],
                    "year_created": this_landmark["year_created"],
                    "address": this_landmark["address"],
                    "created_at": this_landmark["landmarks.created_at"],
                    "updated_at": this_landmark["landmarks.updated_at"],
                }
                # Create the Landmark object
                this_landmark_obj = landmark.Landmark(new_landmark_dictionary)
                # Link the Landmark to this City
                this_city_object.landmarks.append(this_landmark_obj)
            # Return this City with Landmarks attached
            return this_city_object
    
    # Edit one city
    @classmethod
    def edit_city(cls, data):
        query = """
        UPDATE cities SET
        name = %(name)s,
        mayor = %(mayor)s,
        population = %(population)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Delete one city
    @classmethod
    def delete_city(cls, data):
        query = "DELETE FROM cities WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @staticmethod
    def validate_city(form_data):
        is_valid = True # Assume everything is good unless we find a problem
        print(form_data)
        # Perform our checks individually
        if len(form_data["name"]) < 2:
            flash("Name must be 2 or more characters")
            is_valid = False
        if form_data["population"] == "" or int(form_data["population"]) <= 0: # Challenge: figure out to grab the current year
            flash("Population must not be negative")
            is_valid = False
        if len(form_data["mayor"]) < 4:
            flash("Mayor must be 4 or more characters")
            is_valid = False
        return is_valid

