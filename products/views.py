from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorates import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''
class homepage(request):
    return render(request, 'homepage.html')

class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_menu(request):
    menu_data=[
        {"name":"Margherite Pizza", "description":"Classic pizza with tomato sauce and mozzarella cheese","price":8.99},
        {"name":"Veggie Burger","description":"Burger with fresh vegetables and cheese","price":6.49},
        {"name":"Pasta Alfredo","description":"Creamy white sauce pasta with herbs","price":7.99}
    ]
    return Response(menu_data)