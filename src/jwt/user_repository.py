import os
os.chdir('/home/ndc/repos/jwt/src')
import pymongo
import constants
from User import User
#from werkzeug.security import safe_str_cmp

myclient = pymongo.MongoClient(constants.DATABASE_IP,constants.DATABASE_PORT)
db = myclient[ "usersDB"]
users = db[ "users"]

def find_user(username, collection = users):
        query = collection.find_one({'username': username})
        return User.User(query)