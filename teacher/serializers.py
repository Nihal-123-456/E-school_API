from rest_framework import serializers
from .models import *

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    topics_name = serializers.StringRelatedField(source='topics', many=True)
    class Meta:
        model = CourseModel
        fields = ['id','teacher', 'image', 'title', 'topics', 'topics_name', 'description', 'price', 'discount', 'date']