import datetime

from django.db import connection

from adminn.models.userModels import UserOperationClass
from utility.cursorutil import dictfetchall


class UserEventClass():
    def __init__(self, request_object):
        self.request_object = request_object
        self.cursor = connection.cursor()
        self.instance = UserOperationClass(request_object)

    def __del__(self):
        self.cursor.close()

    def login_event(self):
        """ Checks if the username and password matches in the database
            Returns username as a dictionary """
        ''' Sercan : 12.07.2017'''
        t1 = self.request_object['username']
        t2 = self.request_object['password']
        if ("'" in t1 or "'" in t2):
            return False
        self.cursor.execute(
            "SELECT username, admin_id FROM users WHERE username='{}' AND password='{}'".format(t1, str(t2)))
        user = dictfetchall(self.cursor)
        return user

    def register_event(self):
        """ User registration: if user already exists in the database
         It return False, otherwise does the registration """
        ''' Sercan : 13.07.2017 '''
        t1 = self.request_object['username']
        t2 = self.request_object['email']
        t3 = self.request_object['password']
        t4 = self.request_object['name']
        t5 = self.request_object['surname']
        full_name = t4 + " " + t5

        if self.instance.check_user() is False:
            self.cursor.execute("INSERT INTO users (username, email, password, full_name, status_id, admin_id)"
                                "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(t1, t2, str(t3), full_name, 1, 2))
            self.cursor.execute("COMMIT;")
        else:
            return False

    def update_lastlogin(self, username):
        """ Gets the username and updates its last login time """
        ''' Sercan : 14.07.2017 '''
        now = datetime.datetime.now()
        self.cursor.execute("UPDATE users SET lastlogin='{}' WHERE username='{}' ".format(now, username))
        self.cursor.execute("COMMIT;")
