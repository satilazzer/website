from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.base, name = 'base'),
    path('choose_city', views.choose_city, name = 'choose_city'),
    path('zapis', views.zapis, name = 'zapis')
]
