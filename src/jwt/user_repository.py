import os
os.chdir('/home/ndc/repos/jwt/src')
import pymongo
import constants
from User import User
#from werkzeug.security import safe_str_cmp

myclient = pymongo.MongoClient(constants.DATABASE_IP,constants.DATABASE_PORT)
db = myclient["usersDB"]
users = db['users']
users.insert_one({'name': 'admin', 'password': '123456', 'email': 'test@test.com'})

def find_user(email, collection = users):
        query = collection.find_one({'email': email})
        return User.User(query)