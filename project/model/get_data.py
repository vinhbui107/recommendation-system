import pandas as pd


def get_users_data():
    """
    Get demographic data of users
    Output: matrix users
    """
    _user_cols = ["user_id", "age", "sex", "occupation"]
    users = pd.read_csv("../data/users.csv", sep="|", names=_user_cols)

    return users


def get_rating_data():
    """
    Get rating_test data
    Output: dataframe rating_test
    """
    _rating_cols = ["user_id", "movie_id", "rating"]
    rating_test = pd.read_csv(
        "../data/ratings.csv", sep="\t", names=_rating_cols, encoding="latin-1"
    )
    return rating_test
