from flask_app.config.mysqlconnection import connectToMySQL

class Director:
    db_name = "directors_movies_schema" # Class variable holding the schema we're accessing 
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.birthdate = data["birthdate"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.movies = []

    # Your queries will go here.  "INSERT INTO ...."  These will be class methods
    # @classmethod
    # Add this director to the database
    @classmethod
    def add_director(cls, data):
        query = """
        INSERT INTO director 
        (first_name, last_name, birthdate) 
        VALUES 
        (%(first_name)s, %(last_name)s, %(birthdate)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Grab all directors
    @classmethod
    def get_all_directors(cls, data):
        # Query to grab all the directors from the database
        query = "SELECT * FROM directors;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # Return a list of objects back
        list_of_director_instances = []
        if len(results) == 0:
            return [] # Return an empty list if there's nothing there
        else:
            # Go through each dictionary - or each row - from our results
            for this_director_dictionary in results:
                list_of_director_instances.append(cls(this_director_dictionary))
            return list_of_director_instances

    # Grab one director (WITHOUT any movies)
    @classmethod
    def grab_one_director(cls, data):
        query = "SELECT * FROM directors WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0: # If we get nobody back
            return None
        else:
            return cls(results)
    
    @classmethod
    def edit_director(cls, data):
        query = """
        UPDATE directors SET 
        first_name = %(first_name)s, last_name = %(last_name)s, 
        birthdate = %(birthdate)s WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_director(cls, data):
        query = "DELETE FROM directors WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def grab_one_director_with_all_movies(cls, data):
        query = "SELECT * FROM directors LEFT JOIN movies ON director.id = movies.directors_id WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None # Return None as we can only get at most one item
        else:
            # Create the Director
            this_director_instance = cls(results) # Only holds data for the Director itself
            # Loop through each movie and then link to the list of movies for this Director
            for this_movie_dictionary in results:
                """
                Create a movie 
                """
                # Create a new dictionary for the director data
                new_movie_dictionary = {
                    "id": this_movie_dictionary["id"],
                    "title": this_movie_dictionary["title"],
                    "genre": this_movie_dictionary["genre"],
                    "release_date": this_movie_dictionary["release_date"],
                    "box_office": this_movie_dictionary["box_office"],
                    "created_at": this_movie_dictionary["created_at"],
                    "updated_at": this_movie_dictionary["updated_at"],
                }
                # Creating a Movie
                this_movie_instance = cls(new_movie_dictionary)
                # Add this Movie to the list of movies for this Director
                this_director_instance.movies.append(this_movie_instance)
            # Return the Director - with all Movies linked
            return this_director_instance
