from django.shortcuts import render, redirect
from .models import Master
from .models import Center


# Create your views here.
def base(request):
    try:
        city = request.session['city']
    except:
        city = 'Dubai'
        pass
    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    return render(request, 'main/base.html', {'city': city, 'all_cities': all_cities})


def choose_city(request):
    all_cities = {'Dubai': 'https://booking.setmore.com/scheduleappointment/899f7131-6363-43b4-b47f-7f84d8dc6fe6',
                  'Abu-Dhabi': 'https://booking.setmore.com/scheduleappointment/899f7131-6363-43b4-b47f-7f84d8dc6fe6',
                  'Muscat': 'https://booking.setmore.com/scheduleappointment/899f7131-6363-43b4-b47f-7f84d8dc6fe6'}

    city = request.POST['cities']
    request.session['city'] = city
    city = request.session['city']
    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    return render(request, 'main/base.html', {'city': city, 'all_cities': all_cities})


def zapis(request):
    all_cities = {'Dubai': 'https://booking.setmore.com/scheduleappointment/899f7131-6363-43b4-b47f-7f84d8dc6fe6',
                  'Abu-Dhabi': 'https://booking.setmore.com/scheduleappointment/899f7131-6363-43b4-b47f-7f84d8dc6fe6',
                  'Muscat': 'https://booking.setmore.com/scheduleappointment/899f7131-6363-43b4-b47f-7f84d8dc6fe6'}
    city = request.POST['cities']
    return redirect(all_cities[city])
