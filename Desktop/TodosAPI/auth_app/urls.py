from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  UserCreateView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
]
