from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class OwnedCoursesView(viewsets.ModelViewSet):
    queryset = OwnedCoursesModel.objects.all()
    serializer_class = OwnedCoursesSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        course = self.request.query_params.get('course_id')
        user = self.request.query_params.get('user_id')
        if course:
            queryset = queryset.filter(course=course)
        elif user:
            queryset = queryset.filter(student=user)
        return queryset

class WishlistView(viewsets.ModelViewSet):
    queryset = WishlistModel.objects.all()
    serializer_class = WishlistSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.query_params.get('user_id')
        if user:
            queryset = queryset.filter(student=user)
        return queryset

class CartView(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.query_params.get('user_id')
        if user:
            queryset = queryset.filter(student=user)
        return queryset

class ReviewView(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        course = self.request.query_params.get('course_id')
        if course:
            queryset = queryset.filter(course=course)
        return queryset

