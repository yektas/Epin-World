from django.shortcuts import render, redirect,render_to_response
from django.http import HttpResponse
from .models import EventClass
import shutil

####AUTHENTICATION METHODS


def login(request):
    """ Login view: if the user is logged redirects to the index,
    if the user is not logged shows login page """
    ''' Sercan : 11.07.2017 '''

    if 'is_logged' not in request.session:
        return render(request, "login.html")
    else:
        username = request.session['username']
        if request.session['is_logged'] == False:
            instance = EventClass(request)
            instance.update_lastlogin(username)
        return redirect("users:index")


def auth_login(request):
    """ Login Authentication: gets the user's username and password
      from the html form with POST method and checks the database,
      if user exists, username, password and is_logged variables are
      passed to the session. Then redirects to the index page.
      if user does not exits reloads the login page """
    ''' Sercan : 11.07.2017 '''
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
    """ Registration of the user: gets the user's credentials
      from the html form with POST method and checks the database,
      if user already exists, displays warning message
      if user does not exits and registration is successfull, display ok message """
    ''' Sercan : 12.07.2017 '''

    if request.method == "POST":
        user_info = request.POST
        instance = EventClass(user_info)
        if instance.register_event() is False:
            # Registration Failed HTML oluşturulacak.
            return HttpResponse("<h1>Registration Failed</h1>")
        else:
            return HttpResponse("<h1>Registration Successfull</h1>")
    return render(request, "register.html")


def profile(request):
    """ User profile page: gets the username from the session and
     passes the user information to profile.html to show in html """
    ''' Sercan : 13.07.2017 '''
    instance = EventClass(request)
    user_info = instance.find_user(request.session['username'])
    if user_info is not False:
        user = user_info
    return render(request, "profile.html", {'user': user})




def detail_of_game(request,product_name):
    instance = EventClass(request)
    metada_data = instance.get_metadata_of_game(product_name)
    return render_to_response("detail.html",{'game_money_price':metada_data['game_money_price'],'game_name':metada_data['game_name'],'content':metada_data['content']})







#nce = EventClass(request)
  #
   # return render_to_response("detail.html",{'game_money_price':metada_data['game_money_price'],'game_name':metada_data['game_name'],'content':metada_data['content']})

def oyunekle_finish(request):
    game_name = request.POST.get('game_name','')
    game_money_price = request.POST.get('game_money_price','')
    game_genre = request.POST.get('game_name','')
    game_platform = request.POST.get('platform','')

    instance = EventClass(request)
    instance.game_insert(game_name, game_money_price, game_genre, game_platform)

    return render(request,"index.html")


def oyunekle(request):
    game_name = request.POST.get('game_name')
    game_money_count  = request.POST.get('game_money_count')


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
    """ Logs outs the user by deleting session information
        and renders logout.html """
    ''' Sercan : 13.07.2017 '''
    try:
        request.session.flush()
    except KeyError:
        pass
    return render(request, "logout.html")


def create_company(request):
    if request.method == "POST":
        name = request.POST.get('cname', "")
        comp_info = request.POST
        instance = EventClass(comp_info)
        instance.create_company()
        return HttpResponse("<h1>Creating Successful!</h1>")

    return render(request, "company.html")


def user_list(request):
    """ Lists all users in admin panel """
    ''' Sercan : 13.07.2017 '''
    instance = EventClass(request)
    users = instance.list_users()
    return render(request, "userslist.html", {'users': users})


def delete_user(request):
    """ Deletes user """
    ''' Sercan : 13.07.2017 '''
    request.POST.get()
    instance = EventClass(request)
    instance.delete_user()
    return redirect("users:user_list")
