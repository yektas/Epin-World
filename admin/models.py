from django.db import models, connection


# Create your models here.

class AdminModel():

    def __init__(self):
        self.cursor = connection.cursor()

    def CompanyCreate(self):

    