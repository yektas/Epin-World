from django.db import models, connection


# Create your models here.

class AdminEvent:
    def __init__(self):
        self.cursor = connection.cursor()

    def __del__(self):
        self.cursor.close()

    def dictfetchall(self):
        """ Returns all rows from a cursor as a dict """
        ''' Stackoverflow dan alındı. '''
        desc = self.cursor.description
        return [dict(zip([col[0] for col in desc], row))
                for row in self.cursor.fetchall()]

    def create_company(self, name):
        try:
            self.cursor.execute("INSERT INTO company (name) VALUES ('{}')".format(str(name)))
            return True
        except:
            return False

    def list_company(self):

        try:
            self.cursor.execute("select name from company")

        except:
            return False
        company = self.dictfetchall()
        return company

    def create_game(self, companyName, name, platformName, genreName, price):
        try:

            self.cursor.execute("select id from company WHERE name = '{}'".format(str(companyName)))
            companyId = self.cursor.fetchone()[0]
            self.cursor.execute("select id from platform WHERE name = '{}'".format(str(platformName)))
            platformID = self.cursor.fetchone()[0]
            self.cursor.execute("select id from genre WHERE name = '{}'".format(str(genreName)))
            genreID = self.cursor.fetchone()[0]

            self.cursor.execute("INSERT INTO game (name, company_id, platform_id, price, genre_id )"
                                " VALUES ('{}',{},{},{},{})".format(str(name),companyId,platformID,price,genreID))

            return True
        except:
            return False



    def list_platform(self):

        try:
            self.cursor.execute("Select name from platform")

        except:
            return False

        platform = self.dictfetchall()
        return platform

    def list_category(self):

        try:
            self.cursor.execute("Select name from genre")

        except:
            return False

        category = self.dictfetchall()
        return category

    def list_game(self):

        try:
            self.cursor.execute("Select * from game")

        except:
            return False

        game=self.dictfetchall()
        return game




