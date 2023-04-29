from rest_framework import serializers
from .models import *

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class AudioSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    class Meta:
        model = Audio
        fields = '__all__'
