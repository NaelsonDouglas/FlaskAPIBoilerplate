import os
os.chdir('/home/ndc/repos/FlaskAPIBoilerplate/src/jwt')
import pymongo
import constants
from User import User

import api

api.app.run()