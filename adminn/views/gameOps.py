import datetime
import logging

from PIL import Image
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import redirect, render

from adminn.models.companyModels import CompanyEventClass
from adminn.models.gameModels import GameEventClass
from utility.decorators import is_admin, language_assigned

game_instance = GameEventClass()
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

@language_assigned
@is_admin
def add_game(request):
    company_instance = CompanyEventClass(request)
    if request.method == 'POST':
        handle_uploaded_file(request.FILES.get('game_logo'), str(request.FILES.get('game_logo')))
        logo = "images/" + str(request.FILES.get("game_logo"))
        name = request.POST.get('game_name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        company = request.POST.get('company')
        platform = request.POST.get('platform')

        if game_instance.create_game(company, name, platform, category, price, logo):
            logging.info('games added / {}'.format(datetime.datetime.now()))
            return redirect("adminn:index")
        else:
            logging.warning('games could not be added. / {}'.format(datetime.datetime.now()))
            return redirect("adminn:add_game")

    company = company_instance.list_company()
    platform = game_instance.list_platform()
    category = game_instance.list_category()
    return render(request, "{}/add_game.html".format(request.COOKIES['language']),
                  {"company": company,
                   "category": category,
                   "platform": platform}
                  )


@language_assigned
@is_admin
def list_game(request):
    game = game_instance.list_game()
    page = request.GET.get('page', 1)
    """All game split into 5 pieces"""
    paginator = Paginator(game, 5)
    try:
        game = paginator.page(page)
        """If page not an integer return page 1"""
    except PageNotAnInteger:
        game = paginator.page(1)
    except:
        game = paginator.page(paginator.num_pages)

    return render(request, "{}/list_game.html".format(request.COOKIES['language']), {"game": game})


@language_assigned
@is_admin
def delete_game(request):
    if request.method == "POST":
        gname = request.POST.get('name', '')
        game_instance.delete_game(gname)
        logging.info('games deleted / {}'.format(datetime.datetime.now()))
        return redirect("adminn:list_game")
    return redirect("adminn:list_game")


def handle_uploaded_file(file, filename):

    img = Image.open(file)
    img.save("./home/static/images/" + filename)
