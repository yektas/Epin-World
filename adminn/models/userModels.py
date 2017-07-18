from django.db import connection

from utility.cursorutil import dictfetchall


class UserOperationClass():
    def __init__(self, request_object):
        self.request_object = request_object
        self.cursor = connection.cursor()

    def __del__(self):
        self.cursor.close()

    def check_user(self):
        """ Check whether the corresponding user exists or not
            If user exists returns True, if not returns False """
        ''' Sercan : 13.07.2017 '''
        t1 = self.request_object['username']
        t2 = self.request_object['email']

        self.cursor.execute("SELECT username FROM users WHERE username='{}' or email='{}'".format(t1, str(t2)))
        user = dictfetchall(self.cursor)
        if len(user) <= 0:
            return False
        else:
            return True

    def list_users(self):
        """ Returns all users as a list of dictionaries"""
        ''' Sercan : 13.07.2017 '''
        self.cursor.execute("SELECT username, email, full_name, status_id FROM users")
        users = dictfetchall(self.cursor)
        return users

    def delete_user(self, username):
        """ Deletes the user for given username """
        ''' Sercan : 13.07.2017 '''
        if self.check_user() is False:
            self.cursor.execute("DELETE FROM users WHERE username= '{}' ".format(username))
            self.cursor.execute("COMMIT;")

    def find_user(self, username):
        """ Gets the user for given username and returns user
            Returns false if the user does not exist """
        ''' Sercan : 13.07.2017 '''
        self.cursor.execute("SELECT email, full_name FROM users WHERE username='{}'".format(username))
        user = dictfetchall(self.cursor)
        if len(user) <= 0:
            return False
        else:
            return user
