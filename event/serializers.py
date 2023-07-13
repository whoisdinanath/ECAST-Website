from rest_framework.serializers import ModelSerializer
from .models import Event, Newsletter


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'time', 'location', 'description', 'slug', 'image', 'registration_required',
                  'registration_deadline', 'max_attendees', 'contact_email', 'featured', 'coming_soon']


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'name', 'email', 'for_event']
