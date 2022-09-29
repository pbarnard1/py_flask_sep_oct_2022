from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import city # Next week, we'll import other models
from flask import flash

class Landmark:
    db_name = "landmarks_schema" # Class variable that holds the schema name

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.year_created = data["year_created"]
        self.address = data["address"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.city = None # Link ONE City

    @classmethod
    def add_landmark(cls, data):
        query = """
        INSERT INTO landmarks
        (name, year_created, address, city_id)
        VALUES
        (%(name)s, %(year_created)s, %(address)s, %(city_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_landmarks(cls):
        query = """
        SELECT * FROM landmarks 
        JOIN cities 
        ON landmarks.city_id = cities.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        all_landmark_objects = [] # Hold all the Landmarks
        if len(results) == 0: # If no landmarks found, return an empty list
            return []
        else: # At least one landmark found
            for this_landmark_dictionary in results:
                # Create the Landmark object
                this_landmark_obj = cls(this_landmark_dictionary)
                # Grab the city info
                this_city_dictionary = {
                    "id": this_landmark_dictionary["cities.id"],
                    "name": this_landmark_dictionary["cities.name"],
                    "mayor": this_landmark_dictionary["mayor"],
                    "population": this_landmark_dictionary["population"],
                    "created_at": this_landmark_dictionary["cities.created_at"],
                    "updated_at": this_landmark_dictionary["cities.updated_at"],
                }
                # Create the City object
                this_city_object = city.City(this_city_dictionary)
                # Link this City to this Landmark
                this_landmark_obj.city = this_city_object
                # Add this Landmark to the list of Landmarks
                all_landmark_objects.append(this_landmark_obj)
            # Return list of Landmarks once we're done
            return all_landmark_objects

    @classmethod
    def get_one_landmark(cls, data):
        query = """
        SELECT * FROM landmarks 
        JOIN cities 
        ON landmarks.city_id = cities.id
        WHERE landmarks.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0: # If no landmarks found, return an empty list
            return None
        else: # At least one landmark found
            # Create the Landmark object
            # IMPORTANT: results is a LIST of dictionaries - so to access a dictionary, we need a numerical index
            # So we go with results[0], i.e. index 0 - the reason why it's 0 is because if the list is not empty, we
            # always get something at index 0
            landmark_dictionary = results[0]
            this_landmark_obj = cls(landmark_dictionary)
            # Grab the city info
            this_city_dictionary = {
                "id": landmark_dictionary["cities.id"],
                "name": landmark_dictionary["cities.name"],
                "mayor": landmark_dictionary["mayor"],
                "population": landmark_dictionary["population"],
                "created_at": landmark_dictionary["cities.created_at"],
                "updated_at": landmark_dictionary["cities.updated_at"],
            }
            # Create the City object
            this_city_object = city.City(this_city_dictionary)
            # Link this City to this Landmark
            this_landmark_obj.city = this_city_object
            # Return list of Landmarks once we're done
            return this_landmark_obj

    # Edit one landmark
    @classmethod
    def edit_landmark(cls, data):
        query = """
        UPDATE landmarks SET
        name = %(name)s,
        year_created = %(year_created)s,
        address = %(address)s,
        city_id = %(city_id)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Delete one landmark
    @classmethod
    def delete_landmark(cls, data):
        query = "DELETE FROM landmarks WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_landmark(form_data):
        is_valid = True # Assume everything is good unless we find a problem
        print(form_data)
        # Perform our checks individually
        if len(form_data["name"]) < 4:
            flash("Name must be 4 or more characters")
            is_valid = False
        # CORRECTED from lecture: it's > 2022, not <= 2022
        if form_data["year_created"] == "" or int(form_data["year_created"]) > 2022: # Challenge: figure out to grab the current year
            flash("Year must be this year or earlier")
            is_valid = False
        if len(form_data["address"]) < 6:
            flash("Address must be 6 or more characters")
            is_valid = False
        return is_valid
