# Create your tests here.
import unittest

from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def AdminPage(self):
        """Admin Page 200 Donduruyor mu"""
        response = self.client.get("/adminn/")
        self.assertEqual(response.status_code, 200)

    def PageNotFound(self):
        """Random bir sayfa 404 veriyor mu"""
        response = self.client.get("/adasdada/")
        self.assertEqual(response.status_code, 404)

    def Login(self):
        """Post degerleri verilen login 200 veriyor mu"""
        self.client.get("/users/login/", {'username': 'sercan', 'password': '12345'})
        session = self.client.session
        print(session["id"])
        self.assertEqual(session['is_logged'], True)

    def SqlInjection(self):
        response = self.client.get("/users/login/", {"username": "' or True --", "password": "asdada"})
        self.assertEqual(response.context['is_logged'], True)
