from decouple import config
import psycopg2
import os
import pandas as pd


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
