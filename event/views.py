from django.shortcuts import render
from .models import Image, Event, Newsletter
# Create your views here.
from rest_framework.generics import CreateAPIView
from .serializers import ImageSerializer, EventSerializer, NewsletterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ImageCreateView(CreateAPIView):
    # upload multiple image to a image gallery at once
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(for_event=self.request.event)


class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(for_event=self.request.event)


class NewsletterCreateView(CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(for_event=self.request.event)
