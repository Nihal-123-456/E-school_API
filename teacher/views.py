from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.
class TopicView(viewsets.ModelViewSet):
    queryset = TopicModel.objects.all()
    serializer_class = TopicSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        topics = self.request.query_params.get('topic_id')
        user = self.request.query_params.get('user_id')
        if topics:
            queryset = queryset.filter(topics=topics)
        elif user:
            queryset = queryset.filter(teacher=user)
        return queryset
