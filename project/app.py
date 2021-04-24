from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

from utils.helpers import connect_db


app = Flask(__name__)


# CORS implemented so that we don't get errors when trying to access the server from a different server location
CORS(app)


# Display hello
@app.route("/")
def home():
    return "Hello from Recommendation System api"


# get movies recommend for user with username
@app.route("/movies/recommend/<username>")
def get_movies_recommend(username):
    # Connect DB
    cur = connect_db()
    if not cur:
        return "Connect Database failed"

    return "It works"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
