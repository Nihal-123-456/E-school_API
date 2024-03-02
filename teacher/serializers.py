from rest_framework import serializers
from .models import *

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    topics = serializers.SlugRelatedField(
        queryset=TopicModel.objects.all(),
        slug_field='name',
        many=True
    )

    class Meta:
        model = CourseModel
        fields = '__all__'

    def to_internal_value(self, data):
        topics_data = data.pop('topics', None)
        instance = super().to_internal_value(data)
        if topics_data is not None:
            topics = []
            for topic_name in topics_data:
                try:
                    topic = TopicModel.objects.get(name=topic_name)
                    topics.append(topic)
                except TopicModel.DoesNotExist:
                    raise serializers.ValidationError(f"Topic with slug '{topic_name}' does not exist.")
            instance['topics'] = topics
        return instance