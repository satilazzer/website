from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('confirm_city/', views.confirm_city, name = 'confirm_city')
]
