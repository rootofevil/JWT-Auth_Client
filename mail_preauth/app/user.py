import jwt
from app import app
import logging

class JwtUser():
    def __init__(self, token):
        user_data = self.validate_token(token)
        if user_data is not None:
            self.is_authenticated = True
            self.set_id(user_data['id'])
            self.set_attributes(fn = user_data['fullname'], 
                                samaccountname = user_data['samaccountname'], 
                                mail = user_data['mail'], 
                                givenname = user_data['givenname'], 
                                sn = user_data['sn'])
        else:
            self.is_authenticated = False
        self.is_active = True
        self.is_anonymous = False
    
    def get_id(self):
        return self.id
        
    def get_fullname(self):
        return self.fullname
        
    def get_givenname(self):
        return self.givenname
        
    def get_sn(self):
        return self.sn
        
    def get_samaccountname(self):
        return self.samaccountname
        
    def get_mail(self):
        return self.mail
        
    def get_attributes(self):
        return {'id': self.get_id(),
                'fullname': self.get_fullname(),
                'givenname': self.get_givenname(),
                'sn': self.get_sn(),
                'samaccountname': self.get_samaccountname(),
                'mail': self.get_mail()
                }
        
    def set_id(self, id):
        self.id = id

    def set_attributes(self, fn, samaccountname, mail, givenname, sn):
        self.samaccountname = samaccountname
        self.fullname = fn
        self.mail = mail
        self.givenname = givenname
        self.sn = sn
    
    def validate_token(self, token):
        with open(app.config.get('PUBLIC_KEY_PATH'), 'r') as key:
            public_key = key.read()
        logging.debug(token)    
        try:
            data = jwt.decode(token, public_key)
        except jwt.exceptions.ExpiredSignatureError:
            return None
        logging.debug(data)
        return data
        
    def debug(self, info):
        self.info = info