from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EventClass

####AUTHENTICATION METHODS

def login(request):
    if 'is_logged' not in request.session:
        return render(request, "login.html")
    else:
        return HttpResponse("<h1>You are already logged in</h1>")


def auth_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user_info = request.POST

        instance = EventClass(user_info)
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
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_info = request.POST

        instance = EventClass(user_info)

        if instance.register_event() is False:
            # Registration Successful HTML oluşturulacak.
            return HttpResponse("<h1>Registration Failed</h1>")
    return render(request, "register.html")


def profile(request):
    user_content = {'username': request.session['username'],
                    'password': request.session['password'],
                    }
    return render(request, "profile.html", user_content)


def oyunekle(request):
    return render(request, "ekle.html")


def oyunsil(request):
    return render(request, "oyunsil.html")


def userslist(request):
    return render(request, "userslist.html")


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
    return HttpResponse("You are logged out")


def login_success(request):
    return HttpResponse("Registration successful!")


def create_Company(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name', "")
            comp_info = request.POST
            instance = EventClass(comp_info)
        except:
            raise "Err"

        instance.CreateModel(name)

        return HttpResponse("<h1>Creating Successful!</h1>")

    return render(request , "company.html")