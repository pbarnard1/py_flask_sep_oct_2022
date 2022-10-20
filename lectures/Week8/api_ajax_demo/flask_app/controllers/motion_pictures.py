from flask_app import app
from flask import render_template, request, jsonify
import requests, os

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=['POST'])
def search_IMDB():
    # print(request.form)
    # print(f"https://imdb-api.com/en/API/SearchTitle/{os.environ.get('IMDB_API_KEY')}/{request.form['title']}")
    # Talk to the API to grab the data we want
    result = requests.get(f"https://imdb-api.com/en/API/SearchTitle/{os.environ.get('IMDB_API_KEY')}/{request.form['title']}")
    # print(result.json())
    return jsonify(result.json()) # Return HTML response with JSON results