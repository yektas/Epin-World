from django.shortcuts import render, render_to_response,HttpResponse
from django.db import connections
import logging
import json
import datetime
##### META DEFINITIONS
cursor = connections['default'].cursor()
logging.basicConfig(filename= 'debug.log' , level= logging.DEBUG)
######fo

####GAMES METHODS

def detail(request):
    return render(request, "list.html")

def fetch_all_game(request):
    game_show_data = {}
    show_game_name=[]
    show_game_price=[]
    logging.info('OYUNLAR ÇEKİLMEYE BAŞLANIYOR ')
    games = cursor.execute("SELECT * FROM game")
    data = cursor.fetchall()

    for i in data:
        show_game_name.append(i[1])
        show_game_price.append(i[2])
    return show_game_name,show_game_price

def games_json(request):
    logging.info('oyun çekme işlemi bitirildi ')

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
