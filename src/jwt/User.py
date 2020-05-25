class User(object):
        def __init__(self, username, password,_id = -1):        
                self.id = _id
                self.username = username
                self.password = password
       

        def __str__(self):
                if (self.id == -1):
                        return 'User(username='+str(self.username)+' password: '+str(self.password)+')'
                return 'User(id='+str(self.id)+' username='+str(self.username)+' password: '+str(self.password)+')'
        
        def  to_dict(self):
                if (self.id == -1):                        
                        return {'username': self.username, 'password': self.password}
                return {'id': self.id, 'username': self.username, 'password': self.password}

        def to_string(self):
                return str(self)
        
        @staticmethod        
        def User(dict):                
                return User(dict["username"],dict["password"],str(dict["_id"]))