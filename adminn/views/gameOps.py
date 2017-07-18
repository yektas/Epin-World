from django.shortcuts import redirect, render

from adminn.models import AdminEventClass
from users.decorators import is_admin, language_assigned

models = AdminEventClass()


@language_assigned
@is_admin
def add_game(request):
    if request.method == 'POST':
        name = request.POST.get('game_name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        company = request.POST.get('company')
        platform = request.POST.get('platform')

        if models.create_game(company, name, platform, category, price):
            return redirect("adminn:index")
        else:
            return redirect("adminn:creategame")

    company = models.list_company()
    platform = models.list_platform()
    category = models.list_category()
    return render(request, "{}/add_game.html".format(request.COOKIES['language']),
                  {"company": company,
                   "category": category,
                   "platform": platform}
                  )


@language_assigned
@is_admin
def list_game(request):
    game = models.list_game()

    return render(request, "{}/list_game.html".format(request.COOKIES['language']), {"game": game})


@language_assigned
@is_admin
def delete_game(request):
    return render(request, "{}/delete_game.html".format(request.COOKIES['language']))
