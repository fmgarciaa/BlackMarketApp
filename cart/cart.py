
class Cart:
    """
    A base cart class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add_item(self, product):
        if(str(product.id) not in self.cart.keys()):
            self.cart[product.id] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),
                'quantity': 1,
                'unit':str(product.unit),
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity']+1
                    break
        self.save_cart()

    def save_cart(self):
        self.session['cart'] = self.cart
        self.session.modified=True

    def delete_item(self, product):
        product.id = str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.save_cart()
    
    def remove_item(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] = value['quantity']-1
                if value['quantity']<1:
                    self.delete_item(product)
                break
        self.save_cart()

    def clean_cart(self):
        self.session['cart']={}
        self.session.modified = True

