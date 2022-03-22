def cart_items(request):
    amount_cart=0
    items_cart=0

    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            amount_cart=amount_cart+float(value['total'])
            items_cart=items_cart+1
    return {
        'amount_cart':amount_cart,
        'items_cart': items_cart,
    }        

