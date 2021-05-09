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


def pred_for_users(users, model_mode=None):
    '''
    This function to train then predict for all users in users list
    @params: 
        users: users to pred
        model_mode: choosing model CF or DF
    '''
    if model_mode == 'DF':
        # DF
        model = DF(USERS, RATE_TRAIN, 25)
        model.fit()
    elif model_mode == 'CF':
        model = CF( RATE_TRAIN, 25)
        model.fit()
        
    result = np.empty((0, 3))
    for user in users:
        predict_ratings_u = model.recommend(user)

        # now we have real and predict rating of current user
        # i will sort predict rating data and get top 20
        # result : top 20 predict rating + real rating (from rate test data)

        predict_ratings_u_sorted = predict_ratings_u[
            predict_ratings_u[:, 2].argsort(kind="quicksort")[::-1][0:30]
        ]
        result = np.append(result, predict_ratings_u_sorted, axis=0)
    return result

def save_result(users, path, model_mode=None):
    '''
    This funtion use to predict and save result to csv file
    '''
    if model_mode == 'DF':
        pd.DataFrame(pred_for_users(users, model_mode='DF'), columns=['user_id', 'movie_id', 'rating']).to_csv(path+'/df.csv')
    elif model_mode == 'CF':
        pd.DataFrame(pred_for_users(users, model_mode='CF'), columns=['user_id', 'movie_id', 'rating']).to_csv(path+'/cf.csv')