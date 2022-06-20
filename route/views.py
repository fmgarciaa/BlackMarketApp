from django.shortcuts import render
from customers.models import Customers
from orders.models import Order
from datetime import datetime


# Create your views here.
def routeview(request):

    try:
        dt2 = request.POST.get('party')
        dt3 = dt2.split('-')
        data_order = {}
        orders = Order.objects.filter(date__year=dt3[0], date__month=dt3[1], date__day=dt3[2]).values_list()

        for order in orders:
            if order[6] == True:
                status = 'Cancelado'
            else:
                status = 'Pendiente'
                
            customer = Customers.objects.filter(id=order[1]).values_list()
            data_order[order[0]] = {
                'name' : customer[0][1],
                'direction' : customer[0][3],
                'distric': customer[0][4],
                'referencia': customer[0][5],
                'phone' :customer[0][2],
                'status' : status,
                'total':order[5]
            }
            

    except:
        return render(request, 'route/index.html', {})
    context = {
        'data': data_order
    }
    return render(request, 'route/index.html', context)


def get_route(request, date):
    print(request)
    return render(request, 'route/index.html', {})
    