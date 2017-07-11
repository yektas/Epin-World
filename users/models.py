from django.db import connection
cursor = connection.cursor()

class EventClass():

    def __init__(self, request_object):
        self.request_object = request_object
    def login_event(self):
        try:
            cursor.execute("SELECT * FROM users WHERE username= %s", [self.request_object['username']] )
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