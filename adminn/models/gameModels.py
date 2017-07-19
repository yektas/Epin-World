from django.db import connection

from utility.cursorutil import dictfetchall


class GameEventClass():
    def __init__(self):
        self.cursor = connection.cursor()

    def __del__(self):
        self.cursor.close()

    def create_game(self, companyName, name, platformName, genreName, price):
        try:

            self.cursor.execute("select id from company WHERE name = '{}'".format(str(companyName)))
            companyId = self.cursor.fetchone()[0]
            self.cursor.execute("select id from platform WHERE name = '{}'".format(str(platformName)))
            platformID = self.cursor.fetchone()[0]
            self.cursor.execute("select id from genre WHERE name = '{}'".format(str(genreName)))
            genreID = self.cursor.fetchone()[0]

            self.cursor.execute("INSERT INTO game (name, company_id, platform_id, price, genre_id )"
                                " VALUES ('{}',{},{},{},{})".format(str(name), companyId, platformID, price, genreID))

            self.cursor.execute("COMMIT;")
            return True
        except:
            return False

    def get_metadata_of_game(self, game_name):
        self.cursor.execute("SELECT * FROM game WHERE name = {}").format(game_name)
        meta_data = self.cursor.fetchall()
        meta_data_json = []
        for i in meta_data:
            meta_data_json.append(
                {'game_name': '{}'.format(i[1]), 'game_money_price': '{}'.format(i[2]), 'game_content': format(i[9])})

        return meta_data_json

    def game_insert(self, game_name, game_money_price, genre, platform):
        self.cursor.execute(
            "insert into game(name,price,genre_id,company_id,content,platform_id) values('{}',{},1,13,'EhisteGame',1)".format(
                game_name, game_money_price))
        self.cursor.execute("COMMIT;")

    def list_platform(self):
        try:
            self.cursor.execute("Select name from platform")

        except:
            return False

        platform = dictfetchall(self.cursor)
        return platform

    def list_category(self):
        try:
            self.cursor.execute("Select name from genre")

        except:
            return False

        category = dictfetchall(self.cursor)
        return category

    def list_game(self):
        try:
            self.cursor.execute("Select * from game")

        except:
            return False

        game = dictfetchall(self.cursor)
        return game

    def delete_game(self, gname):
        try:
            if (self.check_game(gname)):
                self.cursor.execute("start transaction;")
                self.cursor.execute("delete from game where name='{}' ".format(str(gname)))
                self.cursor.execute("commit;")
                return True
            else:
                return False
        except:
            return False

    def check_game(self, gname):

        self.cursor.execute("SELECT name FROM game WHERE name='{}' ".format(gname))
        company = dictfetchall(self.cursor)
        if len(company) <= 0:
            return False
        else:
            return True
