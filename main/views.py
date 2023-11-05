from django.shortcuts import render, redirect
from .models import Center, Cosmetic


# Create your views here.
def index(request):
    all_cities_booking_links = {'Dubai': 'https://sculptorbyaraykairkanova.setmore.com',
                                'Abu-Dhabi': 'https://sculptorbyaraykairkanovaabudhabi.setmore.com',
                                'Muscat': 'https://sculptor.setmore.com/sculptormuscat'}
    try:
        number_of_items = len(request.session['basket'].keys())
    except:
        number_of_items = 0
    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    try:
        city = request.session['city']
    except:
        city = 'Dubai'
        pass
    request.session['current_page'] = 'index'

    center = Center.objects.get(name=city)
    return render(request, f'main/index.html', {'city': city, 'all_cities': all_cities, 'center': center, 'number_of_items': str(number_of_items), 'center_booking_link': all_cities_booking_links[city]})


def confirm_city(request):
    try:
        request.session['city'] = request.POST['cities']
        current_page = request.session['current_page']
        if current_page == 'index':
            pass
        elif current_page == 'checkout':
            return checkout(request)
        else:
            return marketplace(request)
    except:
        request.session['current_page'] = 'index'
        current_page = request.session['current_page']
    all_cities_booking_links = {'Dubai': 'https://sculptorbyaraykairkanova.setmore.com',
                                'Abu-Dhabi': 'https://sculptorbyaraykairkanovaabudhabi.setmore.com',
                                'Muscat': 'https://sculptor.setmore.com/sculptormuscat'}

    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    number_of_items = len(request.session['basket'])
    request.session['city'] = request.POST['cities']
    city = request.session['city']
    request.session['center_link'] = all_cities_booking_links[city]
    center = Center.objects.get(name=city)
    return render(request, f'main/{current_page}.html', {'city': city, 'all_cities': all_cities, 'center': center, 'center_booking_link': all_cities_booking_links[city], 'number_of_items': str(number_of_items)})


def marketplace(request):
    try:
        number_of_items = len(request.session['basket'].keys())
    except:
        number_of_items = 0
    request.session['current_page'] = 'marketplace'
    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    try:
        city = request.session['city']
    except:
        city = 'Dubai'
        pass
    center = Center.objects.get(name=city)
    cosmetics = Cosmetic.objects.all()
    return render(request, 'main/marketplace.html',
                  {'cosmetics': cosmetics, 'city': city, 'all_cities': all_cities, 'center': center, 'number_of_items': str(number_of_items)})


def checkout(request):
    request.session['current_page'] = 'checkout'
    try:
        number_of_items = len(request.session['basket'].keys())
    except:
        number_of_items = 0
    try:
        basket = request.session['basket']
    except:
        basket = []
    try:
        all_items = [Cosmetic.objects.get(id = str(i)) for i,j in request.session['basket'].items()]
        all_items_number = [str(j) for i, j in request.session['basket'].items()]
    except:
        all_items = []
        all_items_number = []
    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    try:
        city = request.session['city']
    except:
        city = 'Dubai'
        pass
    center = Center.objects.get(name=city)
    shipping_details = request.session['shipping_details']
    total_sum = sum([i.price for i in all_items])
    return render(request, 'main/checkout.html', {'city': city, 'all_cities': all_cities, 'center': center, 'number_of_items': str(number_of_items), 'all_items': all_items, 'all_items_number': all_items_number, 'shipping_details': shipping_details, 'total_sum': total_sum})


def add_item(request, item_id):
    try:
        request.session['basket'][str(item_id)] += 1
    except:
        request.session['basket'] = {}
        request.session['basket'][str(item_id)] = 0
        request.session['basket'][str(item_id)] += 1
    print(request.session['basket'])
    return redirect('../marketplace')


def remove_item(request, item_id):
    del request.session['basket'][str(item_id)]
    return redirect('../checkout')


def change_shipping_info(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    address = request.POST['address']
    city = request.POST['city']
    country = request.POST['country']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    request.session['shipping_details'] = [first_name, last_name, address, city, country, phone_number, email]
    print(request.session['shipping_details'])
    return redirect('../checkout')



def proceed_payment(request):
    pass


def search_item(request):
    search_text = request.POST['search_text']
    try:
        number_of_items = len(request.session['basket'].keys())
    except:
        number_of_items = 0
    request.session['current_page'] = 'marketplace'
    all_cities = ['Dubai', 'Abu-Dhabi', 'Muscat']
    try:
        city = request.session['city']
    except:
        city = 'Dubai'
        pass
    center = Center.objects.get(name=city)
    cosmetics = Cosmetic.objects.filter(description__contains = search_text)
    return render(request, 'main/marketplace.html',
                  {'cosmetics': cosmetics, 'city': city, 'all_cities': all_cities, 'center': center, 'number_of_items': str(number_of_items)})
