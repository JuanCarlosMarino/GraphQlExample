import sys

import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import random
import string

class dbHandler:
    def __init__(self):
        cred = credentials.Certificate("noticias-upb-firebase-adminsdk-i9sx4-aea66b4c67.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        
    def login(self, user, password):
        collection = self.db.collection('users')
        doc = collection.document(user)
        db_user = doc.get().to_dict()

        try:
            if(password == db_user['password']):
                return True
            else:
                return False
        except:
            return False

db = dbHandler()
print(db.login(sys.argv[1], sys.argv[2]))
