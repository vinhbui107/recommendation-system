import numpy as np
import pandas as pd
import gc
import torch

def get_users_data(data, file_name):
    """
    Get demographic data of users
    Output: matrix users
    """
    _user_cols = ["user_id", "age", "sex", "occupation"]
    users = pd.read_csv(
        "./{0}/{1}".format(data, file_name), sep=",",
                dtype={"user_id":int, "age":int}
    )

    return users

def get_items_data():
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
    items = pd.read_csv('./ml-100k/u.item', sep=',', names=_item_cols, encoding='latin-1')

    return items

def get_rating_data(data, file_name):
    """
    Get rating data
    Output: dataframe rating
    """
    _rating_cols = ["user_id", "movie_id", "rating"]
    ratings = pd.read_csv(
        "./{0}/{1}".format(data, file_name),
        sep=",",
        encoding="latin-1",
        dtype={"user_id":int, "movie_id":int}
    )
    return ratings