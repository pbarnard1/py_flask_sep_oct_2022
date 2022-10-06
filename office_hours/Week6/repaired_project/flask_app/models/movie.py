from flask_app.config.mysqlconnection import connectToMySQL

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
    @classmethod
    def grab_all_movies_with_directors(cls, data):
        query = "SELECT * FROM movies JOIN directors ON director.id = movie.directors_id;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
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
                this_director_dictionary = {
                    "id": this_movie_dictionary["id"],
                    "first_name": this_movie_dictionary["first_name"],
                    "last_name": this_movie_dictionary["last_name"],
                    "birthdate": this_movie_dictionary["birthdate"],
                    "created_at": this_movie_dictionary["created_at"],
                    "updated_at": this_movie_dictionary["updated_at"],
                }
                # Creating a Director
                this_director_instance = cls(this_director_dictionary)
                # Link this Director to this Movie
                this_movie_instance.director = this_director_instance
                # Add this Movie to the list after creating and linking
                list_of_movie_instances.append(this_movie_instance)
            return list_of_movie_instances
        
    # Grab one movie with its director
    @classmethod
    def grab_one_movie_with_director(cls, data):
        query = "SELECT * FROM movies JOIN directors ON directors.id = movies.directors_id WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None # Return None as we can only get at most one item
        else:
            # Create the Movie
            this_movie_instance = cls(results) # Only holds data for the movie itself
            """
            Create a director 
            """
            # Create a new dictionary for the director data
            this_director_dictionary = {
                # Table name = table you're joining with - in this case, directors
                "id": results["id"],
                "first_name": results["first_name"],
                "last_name": results["last_name"],
                "birthdate": results["birthdate"],
                "created_at": results["created_at"],
                "updated_at": results["updated_at"],
            }
            # Creating a Director
            this_director_instance = cls(this_director_dictionary)
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
    def delete_movie(cls):
        query = "DELETE FROM movies WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query) 