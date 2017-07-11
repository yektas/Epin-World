from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from .models import EventClass

####AUTHENTICATION METHODS

def login_view(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

def auth_login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user_info = request.POST

    instance = EventClass(user_info)
    user = instance.login_event()
    if user is not None:
        request.session['username'] = username
        request.session['password'] = password
        request.session['email'] = email
        return redirect("users:index")
    '''
    #Eğer bilgiler doğru değilse None dönüyor.
    user = authenticate(username=username, password=password)

    #Burada None olup olmadığını check ediyoruz.
    if user is not None:
       login(request, user)
       return redirect("index")
    else:
       return redirect("users:index")
    '''
def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def profile(request):
    user_content = {'username': request.session['username'],
                    'password': request.session['password'],
                    'email'   : request.session['email']}
    return render(request, "profile.html", user_content)


