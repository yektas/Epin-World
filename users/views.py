from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

def profile(request):
    return render(request,"profile.html")