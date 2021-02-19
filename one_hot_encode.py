import pandas as pd
from get_data import get_items_data, get_users_data, get_rating_data


class OneHotEncode(object):
    def __init__(self, ratings=None, movies=None, users=None):
        self.ratings = ratings
        self.movies = movies
        self.users = users
        self.data_matrix = None
        self.data_features = None

    def _merge_data(self):
        """
        Merge 3 table rating, user and movie using user_id and movie_id
        """
        # merge table rating and user using user_id
        self.data_features = pd.merge(self.ratings, self.users, on="user_id")
        # merge data_features and movies table using movie_id
        self.data_features = pd.merge(self.data_features, self.movies, on="movie_id")

        # divide the age data into a smaller group
        self.data_features["age"] = self.data_features.age.map(
            lambda x: 1
            if int(x) >= 1 and int(x) < 18
            else (
                18
                if int(x) >= 18 and int(x) < 25
                else (
                    25
                    if int(x) >= 25 and int(x) < 35
                    else (
                        35
                        if int(x) >= 35 and int(x) < 45
                        else (45 if int(x) >= 45 and int(x) < 50 else (50 if int(x) >= 50 and int(x) < 56 else 56))
                    )
                )
            )
        )

        # remove field unneed for model
        self.data_features.drop(
            ["zip_code", "timestamp", "movie_title", "release_date", "video_release_date", "imdb_url"],
            axis=1,
            inplace=True,
        )

    def _encode_data_to_binary(self):
        """
        Convert data we just merged to binary
        """
        # convert rating to binary
        self.data_features["rating"] = self.data_features.rating.map(lambda x: 1 if int(x) >= 3 else 0)

        # The get_dummies() function is used to convert categorical variable
        # into dummy/indicator variables.
        self.data_features = pd.get_dummies(self.data_features, columns=["sex", "age", "occupation"])

        # now data_features still have movie_id and user_id
        # maybe we will use it in some case
        # comment or uncomment for remove or keep it
        self.data_features.drop(
            ["user_id", "movie_id"],
            axis=1,
            inplace=True,
        )

        # convert data binary to numpy matrix
        self.data_matrix = self.data_features.to_numpy()

    def fit(self):
        """
        Just for call another function
        """
        # self._clean_data()
        self._merge_data()
        self._encode_data_to_binary()


# yeah we done so i will test it with ml-100k data and have fun
movies = get_items_data("ml-100k", "u.item")
users = get_users_data("ml-100k", "u.user")
ratings = get_rating_data("ml-100k", "u.data")

encode = OneHotEncode(ratings, movies, users)
encode.fit()

print(encode.data_matrix)
print("Number of rows:", encode.data_features.shape[0])
print("Number of columns: ", encode.data_features.shape[1])
