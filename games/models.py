from django.db import connection

from utility.cursorutil import dictfetchall


class GameEventClass:
    def __init__(self):
        self.cursor = connection.cursor()

    def __del__(self):
        self.cursor.close()

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

    def game_search(self, search_text):
        try:
            self.cursor.execute("select name from game where name ilike '%{}%'".format(str(search_text)))
        except:
            return False
        games = dictfetchall(self.cursor)
        return games
