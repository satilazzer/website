from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('marketplace/', views.marketplace, name = 'marketplace'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('add_item/<int:item_id>', views.add_item, name='add_item'),
    path('confirm_city/', views.confirm_city, name = 'confirm_city'),
    path('remove_item/<int:item_id>', views.remove_item, name = 'remove_item'),
    path('change_shipping_info/', views.change_shipping_info, name = 'change_shipping_info'),
    path('proceed_payment/', views.proceed_payment, name = 'proceed_payment'),
    path('search_item/', views.search_item, name = 'search_item')
]
