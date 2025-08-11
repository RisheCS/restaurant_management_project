from django.urls import path
from .views import get_menu, homepage

urlpatterns = [
    path('menu/',get_menu, name='menu'),
    path('', homepage, name='homepage'),
]