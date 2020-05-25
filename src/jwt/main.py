import os
os.chdir('/home/ndc/repos/jwt/src')
import pymongo
import constants
from User import User
from werkzeug.security import safe_str_cmp

import api

api.app.run()