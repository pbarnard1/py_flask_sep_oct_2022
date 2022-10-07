from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import director # Bug fix: need to import other class
class Movie:
    # Bug fix: corrected schema name
    # TIP: Change your schema names at the beginning!!
    db_name = "directors_movies_schema_sep_2022"

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.genre = data["genre"]
        self.release_date = data["release_date"]
        self.box_office = data["box_office"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.director = None

    # Add this movie to the database
    @classmethod
    def add_movie(cls, data):
        query = """
        INSERT INTO movies 
        (genre, title, box_office, release_date, director_id) 
        VALUES 
        (%(genre)s, %(title)s, %(box_office)s, %(release_date)s, %(director_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Grab all movies with directors
    # Bug fix: don't need "data" parameter as the query doesn't require any specific values
    @classmethod
    def grab_all_movies_with_directors(cls):
        # Bug fix: corrected query
        query = "SELECT * FROM movies JOIN directors ON directors.id = movies.director_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        # Return a list of objects back
        list_of_movie_instances = []
        print(results)
        if len(results) == 0:
            return [] # Return an empty list if there's nothing there
        else:
            # Go through each dictionary - or each row - from our results
            for this_movie_dictionary in results:
                # Create the Movie
                this_movie_instance = cls(this_movie_dictionary) # Only holds data for the movie itself
                """
                Create a director 
                """
                # Bug fixes: birth_date, not birthdate; need table name added for duplicate columns
                this_director_dictionary = {
                    "id": this_movie_dictionary["directors.id"],
                    "first_name": this_movie_dictionary["first_name"],
                    "last_name": this_movie_dictionary["last_name"],
                    "birth_date": this_movie_dictionary["birth_date"],
                    "created_at": this_movie_dictionary["directors.created_at"],
                    "updated_at": this_movie_dictionary["directors.updated_at"],
                }
                # Creating a Director - bug fix: Director class, not Movie class (cls() means make a Movie in this case since we're in the Movie class)
                this_director_instance = director.Director(this_director_dictionary)
                # Link this Director to this Movie
                this_movie_instance.director = this_director_instance
                # Add this Movie to the list after creating and linking
                list_of_movie_instances.append(this_movie_instance)
            return list_of_movie_instances
        
    # Grab one movie with its director
    @classmethod
    def grab_one_movie_with_director(cls, data):
        # Bug fix: corrected query
        query = "SELECT * FROM movies JOIN directors ON directors.id = movies.director_id WHERE movies.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None # Return None as we can only get at most one item
        else:
            # Create the Movie
            # Bug fix: need index here to pass in a dictionary
            this_movie_instance = cls(results[0]) # Only holds data for the movie itself
            """
            Create a director 
            """
            # Create a new dictionary for the director data
            this_director_dictionary = {
                # Table name = table you're joining with - in this case, directors
                # Bug fix: directors table needed due to duplicate column names; also need index to reference a dictionary
                "id": results[0]["directors.id"],
                "first_name": results[0]["first_name"],
                "last_name": results[0]["last_name"],
                "birth_date": results[0]["birth_date"], # Bug fix: birth_date, not birthdate
                "created_at": results[0]["directors.created_at"],
                "updated_at": results[0]["directors.updated_at"],
            }
            # Creating a Director
            # Bug fix: need Director class, NOT Movie class
            this_director_instance = director.Director(this_director_dictionary)
            # Link this Director to this Movie
            this_movie_instance.director = this_director_instance
            # Return the Movie - with the Director linked
            return this_movie_instance

    @classmethod
    def edit_movie(cls, data):
        query = """
        UPDATE movies SET title = %(title)s, 
        genre = %(genre)s, release_date = %(release_date)s, 
        box_office = %(box_office)s, director_id = %(director_id)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_movie(cls, data): # Bug fix: need data here and in query_db
        query = "DELETE FROM movies WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data) 