from django.http import HttpResponse
from django.shortcuts import render


def checkout(request):
    product_list = {}

    if 'cart' in request.session:
        product_list = request.session['cart']
    else:
        return HttpResponse("Your cart is empty")

    return render(request, "checkout.html", {'product_list': product_list})


def addtocart(request):
    saved_list = []
    game_data = request.POST.get('game_data', ' ')
    game_data.replace('/\\\g', '')

    print(game_data)
    if 'cart' not in request.session or not request.session['cart']:
        request.session['cart'] = game_data
    else:
        saved_list = request.session.get('cart', [])
        saved_list.append(game_data)
        request.session['cart'] = saved_list
    return render(request, "test.html")
