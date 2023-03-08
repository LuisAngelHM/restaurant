from restaurant import views
from django.urls import path

urlpatterns = [
    path('menu', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view())
]