from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import city # Next week, we'll import other models

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
