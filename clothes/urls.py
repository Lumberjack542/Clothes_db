from django.urls import path
from .views import ShoesApiView, WardrobeApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'shoes', ShoesApiView)
router.register(r'wardrobe', WardrobeApiView)

