
def data_cart(request):
    total_cart=0
    total_items=0
  
    if request.user.is_authenticated and request.session.__contains__('cart'):
        
        
        for key, value in request.session['cart'].items():
            if not key == "is_modify" and not key == 'id_update':
                total_cart = total_cart + float(value['price'])*value['quantity']
                total_items+=1
            
        
    return {
        'total_cart': total_cart,
        'total_items': total_items,  
    }

