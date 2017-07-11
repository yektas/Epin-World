from django.db import connection

cursor = connection.cursor()

class EventClass():

    def __init__(self, request_object):
        self.request_object = request_object
    def login_event(self):
        try:
            cursor.execute("SELECT * FROM users WHERE username= %s", [self.request_object['username']] )
            row = cursor.fetchall()
        finally:
            cursor.close()
        return row