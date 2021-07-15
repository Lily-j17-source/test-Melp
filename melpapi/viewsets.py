from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import View,TemplateView,ListView,CreateView,UpdateView,DetailView
from . import models
from . import serializers
from .models import Restaurant

from .serializers import RestaurantSerializer
# Create your views here.
class RestaurantViewset(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer

    #for list, retrieve-----note

class CreateRestaurantViewset(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
  