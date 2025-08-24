from django.urls import path
from .views import *
from .views import home_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('', home_view, name='homepage'),
]
