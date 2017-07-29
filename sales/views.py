from django.http import HttpResponse
from django.shortcuts import render
import json
from games.models import GameEventClass


def checkout(request):
    product_list = {}

    if 'cart' in request.session:
        product_list = request.session['cart']
    else:
        return HttpResponse("Your cart is empty")

    return render(request, "checkout.html", {'product_list': product_list})


def addtocart(request):

    game_id = request.POST.get('game_id', ' ')
    game_name = request.POST.get('game_name', ' ')
    game_price = request.POST.get('game_price', ' ')

    if 'cart' not in request.session or request.session['cart'] is None:
        quantity = 1
        request.session['cart'] = [{'game_name': game_name, 'game_price': game_price,
                                    'game_id': game_id, 'quantity': quantity}]
    else:
        found = False
        for item in request.session['cart']:
            if game_id == item['game_id']:
                qTemp = int(item['quantity'])
                qTemp += 1
                item['quantity'] = qTemp
                found = True
                break
        if not found:
            game_list = []
            game_list.append({'game_name': game_name, 'game_price': game_price, 'game_id': game_id, 'quantity': 1})
            game_list.extend(request.session['cart'])
            del request.session['cart']
            request.session['cart'] = game_list

    return HttpResponse(json.dumps(request.session['cart']))

def deletecartitem(request):

    game_id = request.POST.get('game_id', ' ')

    for item in request.session['cart']:
        if game_id == item['game_id']:
            game_list = []
            game_list.extend(request.session['cart'])
            for i in game_list:
                if i['game_id'] == game_id:
                    game_list.remove(i)

            del request.session['cart']
            request.session['cart'] = game_list

    return HttpResponse(json.dumps(request.session['cart']))


def cart_json(request):
    instance = GameEventClass()
    if 'cart' in request.session:
        cart = []
        for item in request.session['cart']:
            game = instance.get_game_byid(int(item['game_id']))
            cart.append({'game_name': '{}'.format(game[0]['name']), 'quantity': '{}'.format(item['quantity']),
                         'logo': '{}'.format(game[0]['logo']), 'price': '{}'.format(game[0]['price']), 'game_id': '{}'.format(game[0]['id'])})
        return HttpResponse(json.dumps(cart), content_type='application/json')
    else:
        return False
