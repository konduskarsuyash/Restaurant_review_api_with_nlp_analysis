from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Restaurant, Review
from .serializers import RestaurantSerializer, ReviewSerializer
from .filters import RestaurantFilter  # Import the filter set
from rest_framework.views import APIView
from .leaderboard import Leaderboard
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from django.db.models import F
from .utils import haversine
from rest_framework import status
import logging




class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@swagger_auto_schema(operation_summary='User can do CRUD operations on restaurant ')
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = RestaurantFilter
    ordering_fields = ['average_rating']
    ordering = ['average_rating']
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    


@swagger_auto_schema(operation_summary='User can do CRUD operations on restaurants reviews ')
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['restaurant__name', 'user__username','comment']
    # permission_classes = [IsAuthenticatedOrReadOnly]


@swagger_auto_schema(operation_summary='Top 5 restaurants according to avg rating ')
class LeaderboardView(APIView):
    permission_classes = [AllowAny]  
    def get(self, request):
        leaderboard = Leaderboard('restaurant_leaderboard')
        top_restaurants = leaderboard.get_top_entities(num=5)

        # Fetch restaurant details
        restaurant_details = []
        for restaurant_id, score in top_restaurants:
            try:
                restaurant = Restaurant.objects.get(id=restaurant_id)
                restaurant_details.append({
                    'name': restaurant.name,
                    'average_rating': score
                })
            except Restaurant.DoesNotExist:
                continue

        return Response(restaurant_details)

# logger = logging.getLogger(__name__)


@swagger_auto_schema(operation_summary='Search nearby restaurant using lattitude and longitude fields default radius is set to 10km ')    
class NearbyRestaurantsView(APIView):
    def get(self, request):
        try:
            # Retrieve query parameters
            latitude = request.query_params.get('latitude')
            longitude = request.query_params.get('longitude')
            radius = request.query_params.get('radius', 10)  # Default radius is 10 km

            # Ensure latitude and longitude are provided
            if latitude is None or longitude is None:
                raise ValueError("Latitude and Longitude are required.")

            latitude = float(latitude)
            longitude = float(longitude)
            radius = float(radius)

            nearby_restaurants = []
            for restaurant in Restaurant.objects.all():
                if restaurant.latitude is not None and restaurant.longitude is not None:
                    distance = haversine(latitude, longitude, restaurant.latitude, restaurant.longitude)
                    if distance <= radius:
                        nearby_restaurants.append((restaurant, distance))

            nearby_restaurants.sort(key=lambda x: x[1])

            restaurants = [restaurant[0] for restaurant in nearby_restaurants]

            serializer = RestaurantSerializer(restaurants, many=True)
            return Response(serializer.data)
        except (TypeError, ValueError) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)