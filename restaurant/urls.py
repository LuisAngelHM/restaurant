from restaurant.views import index, menuEspecial
from django.urls import path

urlpatterns = [
    path('menu/<str:day>', index),
    path('menu-especial/<str:day>', menuEspecial),
]