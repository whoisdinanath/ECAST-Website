from rest_framework.serializers import ModelSerializer
from .models import Event, Newsletter, Image


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'time', 'location', 'description', 'slug', 'image', 'registration_required',
                  'registration_deadline', 'max_attendees', 'contact_email', 'featured', 'coming_soon']


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'name', 'email', 'for_event']


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'for_event']
