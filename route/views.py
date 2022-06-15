from django.shortcuts import render

# Create your views here.
def routeview(request):
    
    return render(request, 'route/index.html', {})


def get_route(request, date):
    return render(request, 'route/index.html', {})
    