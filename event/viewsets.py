from rest_framework.viewsets import ModelViewSet
from .models import Event, Newsletter, Image
from .serializers import EventSerializer, NewsletterSerializer, ImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EventViewset(ModelViewSet):
    queryset = Event.objects.all()
    lookup_field = 'slug'
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NewsletterViewset(ModelViewSet):
    queryset = Newsletter.objects.all()
    lookup_field = 'slug'
    serializer_class = NewsletterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ImageViewset(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
