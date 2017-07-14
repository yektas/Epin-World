from django.shortcuts import render, redirect,render_to_response
from django.http import HttpResponse
from .models import EventClass
import shutil

####AUTHENTICATION METHODS


def login(request):
    if 'is_logged' not in request.session:
        return render(request, "login.html")
    else:
        username = request.session['username']
        if request.session['is_logged'] == False:
            instance = EventClass(request)
            instance.update_lastlogin(username)
        return redirect("users:index")


def auth_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user_info = request.POST

        instance = EventClass(user_info)
        instance.update_lastlogin(username)
        user = instance.login_event()


        if len(user) > 0:
            request.session['username'] = username
            request.session['password'] = password
            request.session['is_logged'] = True

            return render(request, "index.html")

        else:
            return redirect("users:login")


def index(request):
    c = {}
    return render(request, "index.html")


def register(request):

    if request.method == "POST":
        user_info = request.POST
        instance = EventClass(user_info)
        if instance.register_event() is False:
            # Registration Successful HTML oluşturulacak.
            return HttpResponse("<h1>Registration Failed</h1>")
    return render(request, "register.html")


def profile(request):
    instance = EventClass(request)
    user_info = instance.find_user(request.session['username'])
    if user_info is not False:
        user = user_info
    return render(request, "profile.html", {'user': user})


<<<<<<< HEAD

def detail_of_game(request,product_name):
    instance = EventClass(request)
    metada_data = instance.get_metadata_of_game(product_name)
    return render_to_response("detail.html",{'game_money_price':metada_data['game_money_price'],'game_name':metada_data['game_name'],'content':metada_data['content']})

=======
def create_html(game_name):
    file_html = open("{}.html".format(game_name.lower()),'w+')
    shutil.copy2("{}.html".format(game_name.lower()).fo, 'templates/products')
>>>>>>> 681fcc9f5c14a0fecf5b0228ab90ebc6e67a7bb7
    pass
 #   instance = EventClass(request)
  #
   # return render_to_response("detail.html",{'game_money_price':metada_data['game_money_price'],'game_name':metada_data['game_name'],'content':metada_data['content']})

<<<<<<< HEAD


def oyunekle_finish(request):
    game_name = request.POST.get('game_name','')
    game_money_price = request.POST.get('game_money_price','')
    game_genre = request.POST.get('game_name','')
    game_platform = request.POST.get('platform','')

    instance = EventClass(request)
    instance.game_insert(game_name,game_money_price,game_genre,game_platform)

    return render(request,"index.html")
=======

def oyunekle(request):
    game_name = request.POST.get('game_name')

    create_html(game_name)
    pass
    return render(request, "ekle.html")
>>>>>>> 681fcc9f5c14a0fecf5b0228ab90ebc6e67a7bb7

def oyunekle_first(request):
    return render(request,"oyunekle.html")

def oyunsil(request):
    return render(request, "oyunsil.html")


def companylist(request):
    return render(request, "companylist.html")


def company(request):
    return render(request, "company.html")


def ordertable(request):
    return render(request, "ordertable.html")


def adminview(request):
    return render(request, "admin.html")


def logout(request):
    try:
        request.session.flush()
    except KeyError:
        pass
    return render(request, "logout.html")


def login_success(request):
    return HttpResponse("Registration successful!")


def create_company(request):
    if request.method == "POST":
        name = request.POST.get('cname', "")
        comp_info = request.POST
        instance = EventClass(comp_info)
        instance.create_company()
        return HttpResponse("<h1>Creating Successful!</h1>")

    return render(request, "company.html")


def user_list(request):

    instance = EventClass(request)
    users = instance.list_users()
    return render(request, "userslist.html", {'users': users})


def delete_user(request):
    request.POST.get()
    instance = EventClass(request)
    instance.delete_user()
    return redirect("users:user_list")