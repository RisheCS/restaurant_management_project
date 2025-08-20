from django.shortcuts import render
from .models import Restaurant

def about_view(request):
    return render(request, 'about.html')
