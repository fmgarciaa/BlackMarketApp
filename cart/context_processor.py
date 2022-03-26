def data_cart(request):
    total_cart=0
    total_items=0
    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            total_cart = total_cart + float(value['price'])*value['quantity']
            total_items= len(request.session['cart'].items())
    return {
        'total_cart': total_cart,
        'total_items': total_items,
    }