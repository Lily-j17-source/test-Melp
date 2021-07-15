from functools import partialmethod
from os import name
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Restaurant(models.Model):
   id = models.CharField(max_length=36,primary_key=True,unique=True,null=False)
   ratin = models.IntegerField()
   name = models.CharField(max_length=32)
   site = models.CharField(max_length=29)
   email = models.CharField(max_length=38, unique=True)
   phone = models.CharField(max_length=12,unique=True)
   street = models.CharField(max_length=27)
   city = models.CharField(max_length=36)
   state = models.CharField(max_length=21)
   lat = models.FloatField(max_length=8)
   lng = models.FloatField(max_length=8)

   def __str__(self):
       return f"{self.id}, {self.ratin},{self.name},{self.site},{self.email},{self.phone},{self.street},{self.city},{self.state},{self.lat},{self.lng}"

   #CRUD
   #CREATE / INSERT / ADD - GET
   #RETRIEVE / FETCH - GET
   #UPDATE / EDIT - PUT
   #DELETE / REMOVE -DELETE
