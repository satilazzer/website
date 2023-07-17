from django.shortcuts import render, redirect
from .models import Center


# Create your views here.
def index(request):
    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    try:
        city = request.session['city']
    except:
        city = 'Dubai'
        pass
    center = Center.objects.get(name = city)
    return render(request, 'main/index.html', {'city': city, 'all_cities': all_cities, 'center': center})


def choose_city(request):
    city = request.POST['cities']
    request.session['city'] = city
    city = request.session['city']
    center = Center.objects.get(name=city)
    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    return render(request, 'main/index.html', {'city': city, 'all_cities': all_cities, 'center': center})


def zapis(request):
    all_cities = {'Dubai': 'https://sculptorbyaraykairkanova.setmore.com',
                  'Abu-Dhabi': 'https://sculptorbyaraykairkanovaabudhabi.setmore.com',
                  'Muscat': 'https://sculptor.setmore.com/sculptormuscat'}
    city = request.POST['cities']
    return redirect(all_cities[city])



