from django.shortcuts import render
from .models import Restaurant

def about_view(request):
    return render(request, 'about.html')
def home_view(request):
    context = {
        "restaurant_name": "Our Restaurant"
    }
    return render(request, "home.html",context)