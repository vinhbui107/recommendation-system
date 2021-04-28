from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

from utils.helpers import connect_db
import os

app = Flask(__name__)


# CORS implemented so that we don't get errors when trying to access the server from a different server location
CORS(app)


# get movies recommend for user with username
@app.route("/")
def home():
    return "Server RS"


# get movies recommend for user with username
@app.route("/movies/recommend/<userId>")
def get_movies_recommend(userId):
    # Connect DB
    cur = connect_db()
    if not cur:
        return "Connect Database failed"

    return userId


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
