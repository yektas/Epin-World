import logging
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from adminn.models.userModels import UserOperationClass
from users.models import UserEventClass
from utility.decorators import language_assigned, login_required

logging.basicConfig(filename='debug.log', level=logging.DEBUG)


@language_assigned
def login(request):
    """ Login view: if the user is logged redirects to the index,
    if the user is not logged shows login page """
    ''' Sercan : 11.07.2017 '''

    if 'is_logged' not in request.session:
        try:
            return render(request, "{}/login.html".format(request.COOKIES['language']))
        except:
            return render(request, "tr/login.html")
    else:
        username = request.session['username']
        if request.session['is_logged'] is False:
            instance = UserEventClass(request)
            instance.update_lastlogin(username)
        return redirect("users:index")


@language_assigned
def logout(request):
    """ Logs outs the user by deleting session information
        and renders logout.html """
    ''' Sercan : 13.07.2017 '''
    try:
        request.session.flush()
        logging.info("logout had done. '{}'".format(datetime.now()))
    except KeyError:
        logging.ERROR('logout had not done')
    return render(request, "{}/logout.html".format(request.COOKIES['language']))


@language_assigned
def register(request):
    """ Registration of the user: gets the user's credentials
      from the html form with POST method and checks the database,
      if user already exists, displays warning message
      if user does not exits and registration is successfull, display ok message """
    ''' Sercan : 12.07.2017 '''

    if request.method == "POST":
        user_info = request.POST
        instance = UserEventClass(user_info)
        if instance.register_event() is False:
            return HttpResponse("<h1>Registration Failed</h1>")
        else:
            return HttpResponse("<h1>Registration Successfull</h1>")
    return render(request, "{}/register.html".format(request.COOKIES['language']))


@language_assigned
@login_required
def profile(request):
    """ User profile page: gets the username from the session and
     passes the user information to profile.html to show in html """
    ''' Sercan : 13.07.2017 '''
    instance = UserOperationClass(request)
    user_info = instance.find_user(request.session['username'])
    if user_info is not False:
        user = user_info
    return render(request, "{}/profile.html".format(request.COOKIES['language']), {'user': user})
