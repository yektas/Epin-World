import json

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

from games.models import GameEventClass


def checkout(request):
    product_list = {}
    total = 0
    if 'cart' in request.session:
        product_list = request.session['cart']
        for item in product_list:
            quantity = int(item['quantity'])
            price = float(item['game_price'])
            subtotal = quantity * price
            item['subtotal'] = subtotal
            total += subtotal
        request.session['cartTotal'] = total
    else:
        return HttpResponse("Your cart is empty")

    return render(request, "checkout.html", {'product_list': product_list})


def update_cart(request):
    game_id = request.POST.get('game_id', ' ')
    newSubtotal = request.POST.get('newSubtotal', ' ')
    quantity = request.POST.get('quantity', ' ')
    if not request.is_ajax() or not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])

    for item in request.session['cart']:
        if item['game_id'] == game_id:
            item['subtotal'] = newSubtotal
            item['quantity'] = quantity
            break
    return HttpResponse('Done')


def addtocart(request):
    game_id = request.POST.get('game_id', ' ')
    game_name = request.POST.get('game_name', ' ')
    game_price = request.POST.get('game_price', ' ')
    logo = request.POST.get('logo', ' ')

    if 'cart' not in request.session or request.session['cart'] is None:
        request.session['cartTotal'] = 0
        quantity = 1
        request.session['cart'] = [{'game_name': game_name, 'game_price': game_price,
                                    'game_id': game_id, 'quantity': quantity, 'logo': logo}]
        request.session['cartTotal'] = game_price
    else:
        found = False
        for item in request.session['cart']:
            if game_id == item['game_id']:
                qTemp = int(item['quantity'])
                qTemp += 1
                item['quantity'] = qTemp
                found = True
                request.session['cartTotal'] = float(request.session['cartTotal']) + float(item['game_price'])
                break
        if not found:
            game_list = []
            game_list.append(
                {'game_name': game_name, 'game_price': game_price, 'game_id': game_id, 'quantity': 1, 'logo': logo})
            game_list.extend(request.session['cart'])
            del request.session['cart']
            request.session['cart'] = game_list
            if 'cartTotal' not in request.session:
                request.session['cartTotal'] = 0
                request.session['cartTotal'] = float(request.session['cartTotal']) + float(game_price)
            else:
                request.session['cartTotal'] = float(request.session['cartTotal']) + float(game_price)
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
            totalPrice = float(item['quantity']) * float(item['game_price'])
            request.session['cartTotal'] = float(request.session['cartTotal']) - float(totalPrice)

    return HttpResponse(json.dumps(request.session['cart']))


def cart_json(request):
    instance = GameEventClass()
    if 'cart' in request.session:
        cart = []
        for item in request.session['cart']:
            game = instance.get_game_byid(int(item['game_id']))
            cart.append({'game_name': '{}'.format(game[0]['name']), 'quantity': '{}'.format(item['quantity']),
                         'logo': '{}'.format(game[0]['logo']), 'price': '{}'.format(game[0]['price']),
                         'game_id': '{}'.format(game[0]['id'])})
        return HttpResponse(json.dumps(cart), content_type='application/json')
    else:
        return False
