from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from reviews.views import LeaderboardView

schema_view = get_schema_view(
   openapi.Info(
      title="Restaurant Reviews API",
      default_version='v1',
      description="This is a REST API for Restaurant reviews",
      contact=openapi.Contact(email="suyashkonduskar27@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('', LeaderboardView.as_view(), name='leaderboard'),
    path("admin/", admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('reviews/', include('reviews.urls')),
    path('swagger<format>.json|.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls.jwt')),
]

