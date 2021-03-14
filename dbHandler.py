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

    def get_random_string(self,length=5):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        #print("Random string of length", length, "is:", result_str)
        return result_str

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



    def get_posts(self):
        collection = self.db.collection('posts')  # opens 'places' collection
        docs = collection.get()
        docs = [doc.to_dict() for doc in docs]
        print(docs)
        return docs
                
    def create_post(self, post_data):
        collection = self.db.collection('posts')
        post_id = self.get_random_string()
        post_data['post_id'] = post_id
        res = collection.document(post_id).set(post_data)
        print(res)

    
    def update_post(self, user, post_id, post_data):

        collection = self.db.collection('posts')
        doc = collection.document(post_id)
        post = doc.get().to_dict()

        if(post['author'] == user):
            collection = self.db.collection('posts')
            res = collection.document(post_id).update(post_data)
            print(res)
    
    def delete_post(self, user, post_id):
        collection = self.db.collection('users')
        doc = collection.document(user)
        user = doc.get().to_dict()

        if(user['isAdmin']):
            # If the user is admin, we can delete right ahead
            collection = self.db.collection('posts')
            collection.document(post_id).delete()
        else:
            # If it is not admin, we need to check that he/she is the author
            # of the post that's trying to delete

            collection = self.db.collection('posts')
            doc = collection.document(post_id)
            post = doc.get().to_dict()

            if(post['author'] == user):
                collection.document(post_id).delete()




## Tests
#db = dbHandler()

# Login
'''
user = 'juanito'
password = 'jojoo'
print(db.login(user, password))
'''

# Get posts
#db.get_posts()

# Create post
'''
date = datetime.datetime.now()
post_data = {
    "name": "Otro post de prueba post",
    "date": date,
    "updated": date,
    "author": "juanito",
    "content": "cositas 3 test"
}
db.create_post(post_data)
'''

# Update post
'''
date = datetime.datetime.now()
post_data = {
    "updated": date,
    "content": "nuevas cositas 22"
}
post_id='dnmyw'
user = 'juanito'
db.update_post(user, post_id, post_data)
'''

# Delete post
'''
post_id='jejeo'
user = 'juanito'
db.delete_post(user, post_id)
'''