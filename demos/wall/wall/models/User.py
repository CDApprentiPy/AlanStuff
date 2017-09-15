from flask import g, request, session
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
class UserManager(object):

    def __init__(self):
        self.db = g.get_db()

    
    def add_user(self, data):
        # add user
        pass
    
    def get_user(self, email, password=False):
        "Returns a specific user object"
        if password:
            # return user with pw_hash - probably login
            query = "SELECT * FROM wall1.users WHERE email = :email"            
        else:
            query = "SELECT first_name, last_name, email, id FROM wall1.users WHERE email = :email"
        data = {
            'email': request.form['email'],
        }
        logee = self.db.query_db(query, data)
        logging.info("Grabbed a User")
        return logee
        # return use withour pw_hash - probably not login