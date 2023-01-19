from django.urls import path
from .views import ShoesApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'shoes', ShoesApiView)


