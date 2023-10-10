from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/')
    registration_required = models.BooleanField(default=False)
    registration_deadline = models.DateField(null=True, blank=True)
    max_attendees = models.PositiveIntegerField(null=True, blank=True)
    contact_email = models.EmailField()
    featured = models.BooleanField(default=False)
    coming_soon = models.BooleanField()
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Newsletter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    for_event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='gallery_images/')
    for_event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='event_image')

    def __str__(self):
        return str(self.for_event.title) + " " + str(self.id)
