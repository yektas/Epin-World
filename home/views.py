from django.shortcuts import render

from adminn.models.gameModels import GameEventClass


def index(request):
    model = GameEventClass()
    platform = model.list_platform()
    pc_games = model.pc_games(1)
    mobil_games = model.mobil_games(2)
    playstation_games = model.playstation_games(3)
    xbox_games = model.xbox_games(4)
    return render(request, "index.html", {"platforms": platform,
                                          "pc_games": pc_games[:5],
                                          "mobil_games": mobil_games,
                                          "xbox_games": xbox_games,
                                          "playstation_games": playstation_games})
