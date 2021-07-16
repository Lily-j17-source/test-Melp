"""restfulapicrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from melpapi.views import CreateRestaurantAPIView, DestroyRestaurantsAPIView, ListRestaurantsAPIView, UpdateRestaurantAPIView
from django.contrib import admin
from django.urls import path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/list/',ListRestaurantsAPIView.as_view(), name='list-restaurants'),
    path('restaurant/create/',CreateRestaurantAPIView.as_view(),name='create-restaurant'),
    path('restaurant/<str:pk>/update/',UpdateRestaurantAPIView.as_view(),name="update-restaurant"),
    path('restaurant/<str:pk>/destroy/',DestroyRestaurantsAPIView.as_view(),name="delete-restaurant")
    #path('api/',include(router.urls))
]
