from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") # Get secret key from .env file
# print(os.environ.get("FLASK_SECRET_KEY"))
# print(os.environ.get("IMDB_API_KEY"))