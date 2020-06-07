import os
os.chdir('/home/ndc/repos/jwt/src')
import pymongo
import constants
from User import User

myclient = pymongo.MongoClient(constants.DATABASE_IP,constants.DATABASE_PORT)
db = myclient["usersDB"]
users = db['users']

users.create_index('email', unique=True)



def create_user(email,name,password, _users=users):
        print("teste")
        newUser = {'name': name, 'password': password, 'email': email}
        _users.insert_one(newUser)
        return User.User(newUser).to_dict()

def find_user(email, collection = users):
        query = collection.find_one({'email': email})
        if query is None:
                return None
        return User.User(query)