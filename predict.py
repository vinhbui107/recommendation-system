import os

import numpy as np
from utils.helpers import (
    export_data,
    get_ratings_data,
    get_users_data,
    pred_for_users,
)


# set python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# export data
print("Export Data...")
export_data()
print("Export Data Done.")


# import data
USERS_DF = get_users_data()
RATINGS_DF = get_ratings_data().values
USERS_DF["user_id"] -= 1
RATINGS_DF[:, :2] -= 1  # start from 0


# switcher
USERS_ARR = USERS_DF.values[:, 0]
USER_FOR_PREDICT_DF = [
    user
    for user in USERS_ARR
    if np.count_nonzero(RATINGS_DF[:, 0] == user) < 10
]
USER_FOR_PREDICT_CF = [
    user for user in USERS_ARR if user not in USER_FOR_PREDICT_DF
]

# predict data cf and save file
print("Predict CF...")
pred_for_users(
    users_df=USERS_DF,
    ratings_df=RATINGS_DF,
    users_for_predict=USER_FOR_PREDICT_CF,
    model_mode="CF",
)
print("Predict CF Done.")


# predcit data df and save file
print("Predict DF...")
pred_for_users(
    users_df=USERS_DF,
    ratings_df=RATINGS_DF,
    users_for_predict=USER_FOR_PREDICT_DF,
    model_mode="DF",
)
print("Predict DF Done.")


# done
print("Finish Process Predict.")
