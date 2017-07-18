import json
import logging

import requests
from django.db import connections
from django.shortcuts import render, HttpResponse

from utility.decorators import language_assigned

logger = logging.getLogger(__name__)
cursor = connections['default'].cursor()


def games_json(request):
    cursor.execute("SELECT * FROM game")

    test_data = cursor.fetchall()
    test_json = []
    for i in test_data:
        test_json.append(
            {'game_id': '{}'.format(i[0]), 'game_name': '{}'.format(i[1]), 'game_money_price': '{}'.format(i[2])})
    return HttpResponse(json.dumps(test_json), content_type='application/json')


# WoodProgrammer
# #Bu method detail.html'i url'den gelen parametreye göre
# generate etmektedir.
# 14/07/17 Cuma.
@language_assigned
def generate_detail_html(request, game_name):
    r = requests.get('http://localhost:8000/games/games_json/')
    games_data = json.loads(r.text)

    detail_html_data = {}

    k = 0
    for i in games_data:

        if str(games_data[k]['game_name']) == '{}'.format(game_name):
            detail_html_data = games_data[k]
            break
        k += 1

    return render(request, 'detail.html', {'game_data': detail_html_data})
