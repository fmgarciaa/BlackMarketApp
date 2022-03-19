class Basket:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        basket=self.session.get('basket')

        if not basket:
            basket=self.session['basket']={}
        else:
            self.basket=basket
    
    def add_item(self, product):
        if(str(product.id) not in self.baket.keys()):
            self.basket[product.id]={
                "id":product.id,
                "name": product.name,
                "price": str(product.price),
                "quantity":1,
            }
        else:
            for key, value in self.basket.items():
                if key==str(product.id):
                    value["quantity"]=value["quantity"]+1
                    break
        self.save_basket()

    def save_basket(self):
        self.session['basket']=self.basket
        self.session.modified=True

    def delete(self, product):
        product.id=str(product.id)
        if product.id in self.basket:
            del self.basket[product.id]
            self.save_basket()

    def remove_item(self, product):
        for key, value in self.basket.items():
                if key==str(product.id):
                    value["quantity"]=value["quantity"]-1
                    if value["quantity"]<1:
                        self.delete(product)
                    break
        self.save_basket()

    def clean_basket(self):
        self.session['basket']={}
        self.session.modified=True



