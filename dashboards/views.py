from django.shortcuts import render
from orders.models import OrderItem, Order
from products.models import Product

def dashboardView(request):
    try:
        dt = request.POST.get('party')
        dt = dt.split('-')
        data_order = {}
        orders = Order.objects.filter(date__year=dt[0], date__month=dt[1], date__day=dt[2]).values_list()
        for order in orders:
            items = OrderItem.objects.filter(order=order[0]).values_list()
            for item in items:
                product = Product.objects.filter(id=item[2])
                quantity = item[3]
                if item[2] in data_order:
                    data_order[item[2]]['quantity'] = data_order[item[2]]['quantity'] + quantity
                else:
                    data_order[item[2]] = {
                        'product': product[0],
                        'quantity' : quantity
                    }
    except:
        return render(request, 'dashboard/index.html',{})
        
    context = {
        'data' : data_order
    }
    return render(request, 'dashboard/index.html',context)
