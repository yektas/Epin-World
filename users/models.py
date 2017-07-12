from django.db import connection

class EventClass():

    def __init__(self, request_object):
        self.request_object = request_object

    def login_event(self):
        """ Checks if the username and password matches in the database
            Returns username as a dictionary
            """
        cursor = connection.cursor()
        t1 = self.request_object['username']
        t2 = self.request_object['password']
        cursor.execute("SELECT username FROM users WHERE username='{}' AND password='{}'".format(t1, str(t2)))
        user = dictfetchall(cursor)
        cursor.close()
        return user

    def register_event(self):
        """ User registration """
        cursor = connection.cursor()

        t1 = self.request_object['username']
        t2 = self.request_object['email']
        t3 = self.request_object['password']
        t4 = self.request_object['name']
        t5 = self.request_object['surname']
        full_name = t4 + " " + t5

        if self.is_user_exists() is False:
            cursor.execute("INSERT INTO users (username, email, password, full_name, status_id, admin_id)"
                           "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(t1, t2, str(t3),full_name, 1, 2))
            temp = cursor.fetchall()
            cursor.commit()
            cursor.close()
        else:
            return False


    def is_user_exists(self):
        """ Check whether the corresponding user exists or not
            If user exists returns True, if not returns False """
        cursor = connection.cursor()
        t1 = self.request_object['username']
        t2 = self.request_object['email']

        cursor.execute("SELECT username FROM users WHERE username='{}' or email='{}'".format(t1, str(t2)))
        user = dictfetchall(cursor)
        if len(user) <= 0:
            return False
        else:
            return True


    def add_game(self):
        cursor = connection.cursor()

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]