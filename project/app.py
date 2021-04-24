from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

from .helpers import connect_db


app = Flask(__name__)


# CORS implemented so that we don't get errors when trying to access the server from a different server location
CORS(app)


def _get_df_recommend(user_id):
    return


def _get_cf_recommend(user_id):
    return


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
