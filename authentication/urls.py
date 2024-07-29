from django.urls import path,include

from . import views

urlpatterns = [

    path('signup/',views.UserCreateView.as_view(),name="sign_up"),
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.jwt')),
]