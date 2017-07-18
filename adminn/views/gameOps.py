from django.shortcuts import redirect, render

from adminn.models.companyModels import CompanyEventClass
from adminn.models.gameModels import GameEventClass
from utility.decorators import is_admin, language_assigned

game_instance = GameEventClass()


@language_assigned
# @is_admin
def add_game(request):
    company_instance = CompanyEventClass(request)
    if request.method == 'POST':
        name = request.POST.get('game_name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        company = request.POST.get('company')
        platform = request.POST.get('platform')

        if game_instance.create_game(company, name, platform, category, price):
            return redirect("adminn:index")
        else:
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
#@is_admin
def list_game(request):
    game = game_instance.list_game()

    return render(request, "{}/list_game.html".format(request.COOKIES['language']), {"game": game})


@language_assigned
@is_admin
def delete_game(request):
    return render(request, "{}/delete_game.html".format(request.COOKIES['language']))
