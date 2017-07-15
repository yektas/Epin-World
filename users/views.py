from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EventClass
from users.decorators import is_admin, login_required
import requests
import json

def language_detector(request):
    language = request.GET.get('language',' ')
    
    request.session['language'] = language
    print("asdassdasdasd " +  request.session['language'] )
    try:
        return render(request, "{}/index.html".format(request.session['language']))
    except:
        return render(request, "tr/index.html".format(request.session['language']))
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
        request.session['admin_id'] = user[0]['admin_id']
        if len(user) > 0:
            request.session['admin_id'] = user[0]['admin_id']
            request.session['username'] = username
            request.session['password'] = password
            request.session['is_logged'] = True

            return redirect("users:index")

        else:
            return redirect("users:login")


def index(request):
    return render(request, "{}/index.html".format(request.session['language']))


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
            return HttpResponse("<h1>Registration Failed</h1>")
        else:
            return HttpResponse("<h1>Registration Successfull</h1>")
    return render(request, "{}/register.html".format(request.session['language']))


@login_required
def profile(request):
    """ User profile page: gets the username from the session and
     passes the user information to profile.html to show in html """
    ''' Sercan : 13.07.2017 '''
    instance = EventClass(request)
    user_info = instance.find_user(request.session['username'])
    if user_info is not False:
        user = user_info
    return render(request, "{}/profile.html".format(request.session['language']), {'user': user})




# WoodProgrammer
# #Bu method detail.html'i url'den gelen parametreye göre
#generate etmektedir.
#14/07/17 Cuma.
def generate_detail_html(request,game_name):
    r = requests.get('http://localhost:8000/games/games_json/')
    games_data = json.loads(r.text)

    detail_html_data = {}

    k = 0
    for i in  games_data:

        if str(games_data[k]['game_name']) == '{}'.format(game_name):
            print(k)
            detail_html_data = games_data[k]

            break

        else:

            print(games_data[0]['game_name'])

        k += 1

    return  render(request, 'detail.html',{'game_data':detail_html_data})

@is_admin
def oyunekle_finish(request):
    game_name = request.POST.get('game_name','')
    game_money_price = request.POST.get('game_money_price','')
    game_genre = request.POST.get('game_name','')
    game_platform = request.POST.get('platform','')

    instance = EventClass(request)
    instance.game_insert(game_name, game_money_price, game_genre, game_platform)

    return generate_detail_html(request,game_name)

@is_admin
def oyunekle_first(request):
    return render(request,"{}/oyunekle.html".format(request.session['language']))

@is_admin
def oyunsil(request):
    return render(request, "{}/oyunsil.html".format(request.session['language']))

@is_admin
def companylist(request):
    return render(request, "{}/companylist.html".format(request.session['language']))

@is_admin
def company(request):
    return render(request, "{}/company.html".format(request.session['language']))

@login_required
def ordertable(request):
    return render(request, "{}/ordertable.html".format(request.session['language']))


@is_admin
def adminview(request):
    return render(request, "{}/admin.html".format(request.session['language']))


def logout(request):
    """ Logs outs the user by deleting session information
        and renders logout.html """
    ''' Sercan : 13.07.2017 '''
    try:
        request.session.flush()
    except KeyError:
        pass
    return render(request, "{}/logout.html".format(request.session['language']))

@is_admin
def create_company(request):
    if request.method == "POST":
        name = request.POST.get('cname', "")
        comp_info = request.POST
        instance = EventClass(comp_info)
        instance.create_company()
        return HttpResponse("<h1>Creating Successful!</h1>")

    return render(request, "{}/company.html".format(request.session['language']))

@is_admin
def user_list(request):
    """ Lists all users in admin panel """
    ''' Sercan : 13.07.2017 '''
    instance = EventClass(request)
    users = instance.list_users()
    return render(request, "{}/userslist.html".format(request.session['language']), {'users': users})

@is_admin
def delete_user(request):
    """ Deletes user """
    ''' Sercan : 13.07.2017 '''
    request.POST.get()
    instance = EventClass(request)
    instance.delete_user()
    return redirect("users:user_list")
