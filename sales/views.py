from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from sales.models import SaleModel
from users.models import EventClass

saleModel = SaleModel()

def checkout(request):
    instance = EventClass(request)
    games = instance.list_games()
    return render(request, "sale.html", {"games":games})


def AddCartView(request):
    """Add Cart Function """
    if request.method == "POST":
        try:
            game_name = request.POST['game']
            hm = request.POST['hm']
        except:
            hm = -1
            game_name = "Diablo1"
    user_name = "sercan"

    saleModel.CreateSaleRow(user_name, game_name, int(hm))
    request.session["game"] = game_name
    return render(request, "sale.html")