from django.db import connection

class EventClass():

    def __init__(self, request_object):
        self.request_object = request_object
    def login_event(self):
        cursor = connection.cursor()
        t1 = self.request_object['username']
        t2 = self.request_object['password']
        temp = cursor.execute("SELECT * FROM users WHERE username='{}' AND password='{}'".format(t1, t2))
        if temp is not None:
            user = dictfetchall(cursor)
            cursor.close()
            return user
        else:
            cursor.close()
            return temp
    def register_event(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username= %s", [self.request_object['username']])
            user = dictfetchall(cursor)
        finally:
            cursor.close()
        return user

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]