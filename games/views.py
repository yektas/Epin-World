from django.shortcuts import render, render_to_response
from django.db import connections
import logging

##### META DEFINITIONS
logger = logging.getLogger(__name__)
cursor = connections['default'].cursor()
######

####GAMES METHODS

def index(request):
    return render(request, "games.html")

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
