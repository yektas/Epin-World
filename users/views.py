from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from .models import EventClass

####AUTHENTICATION METHODS

def login(request):
    if request.session['is_logged'] == True:
        c = {}
        c.update(csrf(request))
        return render(request, 'login.html', c)

def auth_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_info = request.POST

    instance = EventClass(user_info)
    user = instance.login_event()

    if user is not None:
        request.session['username'] = username
        request.session['password'] = password
        request.session['is_logged'] = True
        return redirect("users:index")

    else:
        return redirect("users:login")

def index(request):
    return render(request, "index.html")

def register(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user_info = request.POST

    instance = EventClass(user_info)
    user = instance.register_event()

    return render(request, "register.html")

def profile(request):
    user_content = {'username': request.session['username'],
                    'password': request.session['password'],
                    }
    return render(request, "profile.html", user_content)

def adminview(request):
    return render(request, "admin.html")
def oyunekle(request):
    return render(request, "ekle.html")
def oyunsil(request):
    return render(request, "oyunsil.html")

