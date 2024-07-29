from django.urls import path
from .views import RestaurantViewSet, ReviewViewSet,NearbyRestaurantsView

urlpatterns = [
    # List and create actions for Restaurant
    path('restaurants/', RestaurantViewSet.as_view({"get": "list", "post": "create"}), name='restaurant-list'),
    # Retrieve, update, partial update, and delete actions for Restaurant
    path('restaurants/<int:pk>/', RestaurantViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name='restaurant-detail'),

    # List and create actions for Review
    path('restaurant-reviews/', ReviewViewSet.as_view({"get": "list", "post": "create"}), name='review-list'),
    # Retrieve, update, partial update, and delete actions for Review
    path('restaurant-reviews/<int:pk>/', ReviewViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name='review-detail'),
    
    path('nearby-restaurants/', NearbyRestaurantsView.as_view(), name='nearby-restaurants'),

]
