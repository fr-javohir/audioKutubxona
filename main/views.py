from rest_framework.viewsets import ModelViewSet
from .models import Audio, Topic
from .serializers import AudioSerializer, TopicSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    http_method_names=['get']

class AudioViewSet(ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    http_method_names=['get']

