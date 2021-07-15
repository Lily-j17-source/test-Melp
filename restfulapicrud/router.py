from melpapi.viewsets import CreateRestaurantViewset, RestaurantViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('restaurant',RestaurantViewset)
router.register('restaurant/create/',CreateRestaurantViewset)

#localhost----
#get, put,update,delete
#list,retrieve
