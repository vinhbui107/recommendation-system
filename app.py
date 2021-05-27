import ast
import os

import psycopg2
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

from utils.helpers import connect_db, find_movies_recommend

app = Flask(__name__)


# CORS implemented so that we don't get errors when trying to access the server from a different server location
CORS(app)


# Connect DB
cur = connect_db()


# get movies recommend for user with username
@app.route("/")
def home():
    return "Server RS"


# get movies recommend for user with username
@app.route("/api/recommend/<username>", methods=["GET"])
def get_movies_recommend(username):

    cur.execute(
        "select id from public.user where username = '{}';".format(username)
    )

    user_id = cur.fetchone()

    movies_recommend = find_movies_recommend(user_id["id"])

    if not movies_recommend:
        message = jsonify(message="User not found.")
        return make_response(message, 400)

    movie_ids = movies_recommend.replace("[", "").replace("]", "").split()
    # movie_ids = ast.literal_eval(movie_ids)

    cur.execute(
        "select * from public.movie where id in {}".format(tuple(movie_ids))
    )

    movies = cur.fetchall()

    return jsonify(movies=movies)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
