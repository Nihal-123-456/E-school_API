from rest_framework import serializers
from .models import *

class OwnedCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnedCoursesModel
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistModel
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'