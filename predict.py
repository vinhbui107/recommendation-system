import os

from utils.export_data import export_data
from utils.helpers import (
    get_ratings_data,
    get_users_data,
    pred_for_users,
)


# set python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# export data
print("Export data...")
export_data()

# import data
print("Import data...")
USERS = get_users_data()
RATE_TRAIN = get_ratings_data().values
USERS["user_id"] -= 1
RATE_TRAIN[:, :2] -= 1  # start from 0

# switcher
USER_NOT_RATED = list(set(USERS["user_id"]) - set(RATE_TRAIN[:, 0]))
USER_RATED = set(RATE_TRAIN[:, 0])

# predict data cf and save file
print("Predict CF model...")
pred_for_users(
    users_df=USERS,
    ratings_df=RATE_TRAIN,
    users_for_predict=USER_RATED,
    model_mode="CF",
)

# predcit data df and save file
print("Predict DF model...")
pred_for_users(
    users_df=USERS,
    ratings_df=RATE_TRAIN,
    users_for_predict=USER_NOT_RATED,
    model_mode="DF",
)

# done
print("Predict done.")
