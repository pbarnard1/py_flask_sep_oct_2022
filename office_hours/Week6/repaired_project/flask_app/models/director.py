from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import movie # Bug fix: need to import this to create Movies

class Director:
    db_name = "directors_movies_schema_sep_2022" # Bug fix: need schema name to match
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.birth_date = data["birth_date"] # Bug fix: need column names to match up with those in our ERD
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.movies = []

    # Your queries will go here.  "INSERT INTO ...."  These will be class methods
    # @classmethod
    # Add this director to the database
    @classmethod
    def add_director(cls, data):
        # Bug fix: Table name must match; column names must match
        query = """
        INSERT INTO directors 
        (first_name, last_name, birth_date) 
        VALUES 
        (%(first_name)s, %(last_name)s, %(birth_date)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Grab all directors
    @classmethod
    def get_all_directors(cls): # Bug fix: no need for "data" dictionary because the query doesn't need any values - no %()s
        # Query to grab all the directors from the database
        query = "SELECT * FROM directors;"
        results = connectToMySQL(cls.db_name).query_db(query)
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
        print(results)
        print("Made it here")
        if len(results) == 0: # If we get nobody back
            return None
        else:
            return cls(results[0]) # Bug fix: need index as we need a dictionary, not a list
    
    @classmethod
    def edit_director(cls, data):
        query = """
        UPDATE directors SET 
        first_name = %(first_name)s, last_name = %(last_name)s, 
        birth_date = %(birth_date)s WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_director(cls, data):
        query = "DELETE FROM directors WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def grab_one_director_with_all_movies(cls, data):
        # Bug fixes: corrected query AND updated the movies table to make sure the table name and foreign key are correct
        query = """
        SELECT * FROM directors 
        LEFT JOIN movies 
        ON directors.id = movies.director_id 
        WHERE directors.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None # Return None as we can only get at most one item
        else:
            # Create the Director
            # Bug fix: need [0] as results is a list, but we need a dictionary at index 0
            this_director_instance = cls(results[0]) # Only holds data for the Director itself
            # Loop through each movie and then link to the list of movies for this Director
            for this_movie_dictionary in results:
                """
                Create a movie 
                """
                # Create a new dictionary for the director data
                new_movie_dictionary = {
                    "id": this_movie_dictionary["movies.id"], # Bug fixes: need table name when joining tables where column names are duplicated
                    "title": this_movie_dictionary["title"],
                    "genre": this_movie_dictionary["genre"],
                    "release_date": this_movie_dictionary["release_date"],
                    "box_office": this_movie_dictionary["box_office"],
                    "created_at": this_movie_dictionary["movies.created_at"],
                    "updated_at": this_movie_dictionary["movies.updated_at"],
                }
                # Creating a Movie
                # Bug fix: need movie.Movie to create movie object, NOT cls(), which creates a Director object
                # cls() means create a class instance - or object - of the current class you're in, which is in this case the Director class
                this_movie_instance = movie.Movie(new_movie_dictionary) 
                # Add this Movie to the list of movies for this Director
                this_director_instance.movies.append(this_movie_instance)
            # Return the Director - with all Movies linked
            return this_director_instance
