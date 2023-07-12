from rest_framework.viewsets import ModelViewSet
from .models import Event, Newsletter
from .serializers import EventSerializer, NewsletterSerializer
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
