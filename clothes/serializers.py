from rest_framework import serializers
from .models import Shoes, Wardrobe


class ShoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoes
        fields = '__all__'


class ShoesCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Shoes
        fields = '__all__'


class WardrobeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wardrobe
        fields = '__all__'
