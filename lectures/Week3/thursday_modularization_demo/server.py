from flask_app import app # Brings in the app from the __init__.py file
from flask_app.controllers import cities # IMPORT controllers here

if __name__=="__main__":
    app.run(debug=True)