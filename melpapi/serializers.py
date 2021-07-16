#Api
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id","name"]


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "ratin",
            "name",
            "site",
            "email",
            "phone",
            "street",
            "city",
            "state",
            "lat",
            "lng",
            ]
        def create(self, validate_data):
            print(validate_data)
            restaurant = Restaurant.objects.create_restaurant(**validate_data)

            return restaurant
        def update(self,value):
            pk = value
            qs = Restaurant.objects.filter(id!=pk)
            if qs.exists():
                raise serializers.ValidationError("This pk no exist")
            return pk