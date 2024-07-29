import django_filters
from .models import Restaurant

class RestaurantFilter(django_filters.FilterSet):
    min_rating = django_filters.NumberFilter(field_name='average_rating', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='average_rating', lookup_expr='lte')

    class Meta:
        model = Restaurant
        fields = ['min_rating', 'max_rating']
