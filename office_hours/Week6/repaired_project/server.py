from flask_app import app
# IMPORTANT BUG FIX: Need to import ALL controllers; forget to import movies 
from flask_app.controllers import directors, movies

if __name__=="__main__":
    app.run(debug=True)