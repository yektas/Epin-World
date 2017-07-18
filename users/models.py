from django.db import connection
import datetime
import requests
import json
class EventClass():

    def __init__(self, request_object):
        self.request_object = request_object
        self.cursor = connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.cursor.execute("COMMIT;")

    def login_event(self):
        """ Checks if the username and password matches in the database
            Returns username as a dictionary """
        ''' Sercan : 12.07.2017'''
        t1 = self.request_object['username']
        t2 = self.request_object['password']
        self.cursor.execute("SELECT username, admin_id FROM users WHERE username='{}' AND password='{}'".format(t1, str(t2)))
        user = self.dictfetchall()
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

        if self.check_user() is False:
            self.cursor.execute("INSERT INTO users (username, email, password, full_name, status_id, admin_id)"
                           "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(t1, t2, str(t3),full_name, 1, 2))
        else:
            return False

    def check_user(self):
        """ Check whether the corresponding user exists or not
            If user exists returns True, if not returns False """
        ''' Sercan : 13.07.2017 '''
        t1 = self.request_object['username']
        t2 = self.request_object['email']

        self.cursor.execute("SELECT username FROM users WHERE username='{}' or email='{}'".format(t1, str(t2)))
        user = self.dictfetchall()
        if len(user) <= 0:
            return False
        else:
            return True

    def create_company(self):

        cname = self.request_object['cname']
        if self.check_company() is False:
            self.cursor.execute("INSERT INTO company (name) VALUES ( '{}' )".format(str(cname)))

    def check_company(self):

        cname = self.request_object['cname']
        self.cursor.execute("SELECT name FROM company WHERE name='{}' ".format(cname))
        company = self.dictfetchall()
        if len(company) <= 0:
            return False
        else:
            return True

    def list_users(self):
        """ Returns all users as a list of dictionaries"""
        ''' Sercan : 13.07.2017 '''
        self.cursor.execute("SELECT username, email, full_name, status_id FROM users")
        users = self.dictfetchall()
        return users

    def delete_user(self, username):
        """ Deletes the user for given username """
        ''' Sercan : 13.07.2017 '''
        if self.check_user() is False:
            self.cursor.execute("DELETE FROM users WHERE username= '{}' ".format(username))

    def find_user(self, username):
        """ Gets the user for given username and returns user
            Returns false if the user does not exist """
        ''' Sercan : 13.07.2017 '''
        self.cursor.execute("SELECT email, full_name FROM users WHERE username='{}'".format(username))
        user = self.dictfetchall()
        if len(user) <= 0:
            return False
        else:
            return user

    def update_lastlogin(self, username):
        """ Gets the username and updates its last login time """
        ''' Sercan : 14.07.2017 '''
        now = datetime.datetime.now()
        self.cursor.execute("UPDATE users SET lastlogin='{}' WHERE username='{}' ".format(now, username))


    def dictfetchall(self):
        """ Returns all rows from a cursor as a dict """
        ''' Stackoverflow dan alındı. '''
        desc = self.cursor.description
        return [dict(zip([col[0] for col in desc], row))
                for row in self.cursor.fetchall()]

    def get_metadata_of_game(self,game_name):
        self.cursor.execute("SELECT * FROM game WHERE name = {}").format(game_name)
        meta_data = self.cursor.fetchall()
        meta_data_json = []
        for i in meta_data:
            meta_data_json.append({'game_name':'{}'.format(i[1]),'game_money_price': '{}'.format(i[2]),'game_content': format(i[9])})

        return meta_data_json

    def game_insert(self,game_name,game_money_price,genre,platform):
        self.cursor.execute("insert into game(name,price,genre_id,company_id,content,platform_id) values('{}',{},1,13,'EhisteGame',1)".format(game_name,game_money_price))


    def get_popular_game(self):

        r = requests.get('http://localhost:8000/games/games_json/')
        games_data = json.loads(r.text)

        meta_data_json = []
        k = 0
        for i in  games_data:
            meta_data_json.append({'game_name':i['game_name'],'game_money_count':i['game_money_price']})
            
            k += 1
            if k==4:
                break;

        return  meta_data_json



