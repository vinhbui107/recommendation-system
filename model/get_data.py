import pandas as pd


def get_users_data():
    """
    Get demographic data of users
    Output: matrix users
    """
    users = pd.read_csv(
        "C:/Dev/recommendation-system/model/data/users.csv",
        sep=",",
    )

    return users


def get_ratings_data():
    """
    Get rating_test data
    Output: dataframe rating_test
    """
    rating_test = pd.read_csv(
        "C:/Dev/recommendation-system/model/data/ratings.csv",
        sep=",",
        encoding="latin-1",
    )
    return rating_test


if __name__ == "__main__":

    print(get_users_data())
