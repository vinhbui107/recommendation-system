import pandas as pd
import numpy as np


def get_users_data(data, file_name):
    """
    Get demographic data of users
    Output: matrix users
    """
    _user_cols = ["user_id", "age", "sex", "occupation", "zip_code"]
    users = pd.read_csv("./{0}/{1}".format(data, file_name), sep="|", names=_user_cols)

    return users


def get_items_data(data, file_name):
    """
    Get items data
    Output: dataframe items
    """
    _item_cols = [
        "movie_id",
        "movie_title",
        "release_date",
        "video_release_date",
        "imdb_url",
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children's",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "filmNoir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "SciFi",
        "Thriller",
        "War",
        "Western",
    ]
    items = pd.read_csv("./{0}/{1}".format(data, file_name), sep="|", names=_item_cols, encoding="latin-1")

    return items


def get_rating_data(data, file_name):
    """
    Get rating_test data
    Output: dataframe rating_test
    """
    _rating_cols = ["user_id", "movie_id", "rating", "timestamp"]
    ratings = pd.read_csv("./{0}/{1}".format(data, file_name), sep="\t", names=_rating_cols, encoding="latin-1")
    return ratings
