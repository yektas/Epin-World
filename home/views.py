from django.shortcuts import render, render_to_response, redirect

from adminn.models.gameModels import GameEventClass
from utility.decorators import language_assigned


def language_detector(request):
    if request.method == 'GET':
        try:
            response = render_to_response("{}/index.html".format(request.GET.get('language', ' ')))
            response.set_cookie('language', '{}'.format(request.GET.get('language', ' ')))
            return response
        except:
            response = render_to_response("tr/index.html")
            try:
                response.set_cookie('language', '{}'.format(request.session['language']))
            except:
                response.set_cookie('language', 'tr')
            return response
    else:
        return redirect("home:index")


@language_assigned
def index(request):
    model = GameEventClass()
    platform = model.list_platform()
    pc_games = model.pc_games(1)
    mobil_games = model.mobil_games(2)
    xbox_games = model.xbox_games(3)

    return render(request, "{}/index.html".format(request.COOKIES['language']), {"platforms": platform,
                                                                                 "pc_games": pc_games[:5],
                                                                                 "mobil_games": mobil_games,
                                                                                 "xbox_games": xbox_games})
