from rest_framework import serializers
from .models import Restaurant, Review

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'location', 'city', 'average_rating','latitude','longitude']
        read_only_fields = ['average_rating']

class ReviewSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'sentiment', 'created_at', 'restaurant_name', 'user_name', 'restaurant', 'user']
        read_only_fields = ['sentiment', 'restaurant_name', 'user_name']



