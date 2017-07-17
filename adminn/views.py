from django.shortcuts import render, redirect

# Create your views here.
from adminn.models import AdminEvent

models = AdminEvent()


def admin_index(request):

    return render(request, 'admin.html')


def create_company(request):
    if request.method == 'POST':
        name = request.POST.get('cname',"")
        if(models.create_company(name)):
            return redirect("adminn:index")


    return render(request,'company.html')


def list_company(request):
    company = models.list_company()

    return render(request, 'companylist.html', {"company":company})

def create_game(request):
    if request.method == 'POST':
        name = request.POST.get('game_name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        company = request.POST.get('company')
        platform = request.POST.get('platform')

        if models.create_game(company,name,platform,category,price):
            return redirect("adminn:index")
        else:
            return redirect("adminn:creategame")

    company = models.list_company()
    platform = models.list_platform()
    category = models.list_category()
    return render(request, "add_game.html",
                  {"company":company,
                    "category":category,
                   "platform":platform}
                  )

def list_game(request):

    game = models.list_game()

    return render(request, "list_game.html" , {"game":game})