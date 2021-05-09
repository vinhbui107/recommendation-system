import os

from model import collaborative_filtering, demographic_filtering
from utils.export_data import export_data
from utils.helpers import get_ratings_data, get_users_data, pred_for_users, save_result


# set python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# import data
USERS = get_users_data()
RATE_TRAIN = get_ratings_data().values
USERS['user_id'] -= 1
RATE_TRAIN[:, :2] -= 1 # start from 0

# switcher 
USER_NOT_RATED = list( set(USERS['user_id']) - set(RATE_TRAIN[:,0]) )
USER_RATED = set(RATE_TRAIN[:,0])

# get data
path='/Users/phusdt/GitHub/recommendation-system/model'
# predict data cf and save file
save_result(users=USER_RATED, path=path, model_mode='CF')
# predcit data df and save file
save_result(users=USER_NOT_RATED, path=path, model_mode='DF')
# done
