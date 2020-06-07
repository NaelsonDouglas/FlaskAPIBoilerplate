class User(object):
        def __init__(self, name, password,email,_id = -1):        
                self.id = _id
                self.name = name
                self.password = password
                self.email = email
       

        def __str__(self):
                if (self.id == -1):
                        return 'User(name='+str(self.name)+' password: '+str(self.password)+')'+' email: '+str(self.email)+')'
                return 'User(id='+str(self.id)+' name='+str(self.name)+' password: '+str(self.password)+')'+' email: '+str(self.email)+')'
        
        def  to_dict(self):
                if (self.id == -1):                        
                        return {'name': self.name, 'email':self.email, 'password': self.password}
                return {'id': self.id, 'name': self.name, 'email':self.email, 'password': self.password}

        def to_string(self):
                return str(self)
        
        @staticmethod        
        def User(dict):                
                return User(dict['name'],dict['password'],dict['email'],str(dict['_id']))