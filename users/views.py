from django.shortcuts import render

def profile_view(request):
    template_name = 'profile.html'
    context = {
        "user_name": "Sercan"
    }
    return render(request, template_name, context)

def login(request):
    return render(request, "login.html")

def register(request):

    return render(request, "register.html")