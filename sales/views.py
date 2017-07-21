from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

def checkout(request):
    product_list = {}

    if 'cart' in request.session:
        product_list = request.session['cart']
    else:
        return HttpResponse("Your cart is empty")

    return render(request, "checkout.html", {'product_list': product_list})


def addtocart(request):
    quantity = 0

    game_name = request.POST.get('game_name', ' ')
    game_id = request.POST.get('game_id', ' ')
    game_price = request.POST.get('game_price', ' ')

    game_data = {'game_name': game_name, 'game_id': game_id, 'game_price': game_price, 'quantity': quantity}

    if 'cart' not in request.session or request.session['cart'] is None:
        request.session['cart'] = game_data
        if game_id == request.session['cart']['game_id']:
            request.session['cart']['quantity'] += 1
        elif game_id != request.session['cart']['game_id']:
            temp_list = []
            temp_list = request.session['cart']
            del request.session['cart']
            temp_list.append(game_data)
            request.session['cart'] = temp_list
    return HttpResponse(json.dumps(request.session['cart']))
