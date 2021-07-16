from django.http import response
from melpapi import serializers
from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer,RestaurantListSerializer

class ListRestaurantsAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

class CreateRestaurantAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DestroyRestaurantsAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UpdateRestaurantAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

  