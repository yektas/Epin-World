from django.shortcuts import render, render_to_response,HttpResponse
from django.db import connections
import logging
import json
import requests
##### META DEFINITIONS
logger = logging.getLogger(__name__)
cursor = connections['default'].cursor()
######

####GAMES METHODS

def detail(request):
    return render(request, "list.html")

def fetch_all_game():
    game_show_data = {}
    show_game_name=[]
    show_game_price=[]
    games = cursor.execute("SELECT * FROM games")
    data = cursor.fetchall()
    for i in data:
        show_game_name.append(i[1])
        show_game_price.append(i[2])
    return show_game_name,show_game_price

def games_json(request):
    cursor.execute("SELECT * FROM game")
    
    test_data = cursor.fetchall()
    list_test_data = list(test_data)
    test_json = []
    for i in test_data:
        test_json.append({'game_name':'{}'.format(i[1]),'game_money_price':'{}'.format(i[2])})
    return HttpResponse(json.dumps(test_json), content_type='application/json')




def games(request):
    if request.user.is_authenticated():
        if request.session['language'] == "tr":

            logging.debug("USER {} FETCHED GAMES".format(request.user))
            return render_to_response("tr/oyunlar.html",{"game_data":fetch_all_game()})
        else:
            logging.debug("USER {} FETCHED GAMES".format(request.user))
            return render_to_response("eng/games.html", {"game_data": fetch_all_game()})

    else:
        return render(request, "login.html")



def generate_detail_html(request):
    game_name = request.POST.get('search_game_name',' ')

    r = requests.get('http://localhost:8000/games/games_json/')
    games_data = json.loads(r.text)

    detail_html_data = {}

    k = 0
    for i in  games_data:

        if str(games_data[k]['game_name']) == '{}'.format(game_name):
            print(k)
            detail_html_data = games_data[k]

            break

        else:

            print(games_data[0]['game_name'])

        k += 1

    return  render(request, 'detail.html',{'game_data':detail_html_data})





