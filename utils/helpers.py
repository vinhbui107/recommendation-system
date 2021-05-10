import os

import pandas as pd
import numpy as np
import psycopg2
from decouple import config
from model import collaborative_filtering, demographic_filtering

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def connect_db():
    try:
        # PostgreSQL Database credentials loaded from the .env file
        DB_NAME = config("DB_NAME")
        DB_USER = config("DB_USER")
        DB_PASSWORD = config("DB_PASSWORD")
        DB_HOST = config("DB_HOST")
        DB_PORT = config("DB_PORT")

        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        return conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        return error


def get_users_data():
    """
    Get demographic data of users
    Output: matrix users
    """
    users = pd.read_csv(
        "model/data/users.csv",
        sep=",",
    )
    return users


def get_ratings_data():
    """
    Get rating_test data
    Output: dataframe rating_test
    """
    rating_test = pd.read_csv(
        "model/data/ratings.csv",
        sep=",",
        encoding="latin-1",
    )
    return rating_test


def pred_for_users(users_df, ratings_df, users_for_predict, model_mode=None):
    """
    This function to train then predict for all users in users list
    @params:
        users_df: dataframe of users
        ratings_df: dataframe of rating
        users_for_predict: users for predict
        model_mode: CF or DF
    """
    if model_mode == "DF":
        path = "model/data_predicted/df.csv"
        model = demographic_filtering.DF(users_df, ratings_df, 25)
        model.fit()
    elif model_mode == "CF":
        path = "model/data_predicted/cf.csv"
        model = collaborative_filtering.CF(ratings_df, 25)
        model.fit()

    result = pd.DataFrame(columns=["user_id", "movies"])
    for user in users_for_predict:
        print("Predict for user: {}".format(user))

        # predict ratings for current user
        predict_ratings_u = model.recommend(user)

        # sort predicted ratings
        predict_ratings_u_sorted = predict_ratings_u[
            predict_ratings_u[:, 2].argsort(kind="quicksort")[::-1][0:30]
        ]

        # get array movies recommend
        recommend_items = predict_ratings_u_sorted[:, 1].astype(int)

        # add recommend result to df
        result = result.append(
            {"user_id": user + 1, "movies": recommend_items}, ignore_index=True
        )

    # save to csv file
    result.to_csv(path, index=False)
