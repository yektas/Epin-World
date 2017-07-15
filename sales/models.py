from django.db import connection


class SaleModel():

    def __init__(self):
        self.cursor = connection.cursor()


    def CreateSaleRow(self, username, gameName, count):
        """Find User and Game id and Insert Sale Table"""
        self.cursor.execute("""select id from game where name = '{}'
        """.format(str(gameName)))
        gameId = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT id FROM users WHERE username = '{}' ".format(str(username)))
        userId = self.cursor.fetchone()[0]
        self.cursor.execute("select price from game WHERE name = '{}' ".format(str(gameName)))
        amount = self.cursor.fetchone()[0] * count
        try:
            self.cursor.execute("insert into sale (game_id,user_id,amount) VALUES ('{}','{}',{}) ;".format(gameId,userId,amount))
            return True
        except:
            return False
            """Add Log"""
