from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import ??? # Next week, we'll import other models

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

