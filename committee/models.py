from typing import Any, Dict, Tuple
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.db.models import signals
from django.dispatch import receiver


def member_image_path(instance, filename):
    position = instance.position.replace(" ", "-").lower()
    name = instance.name.replace(" ", "-").lower()
    return f'member/{position}/{name}/{filename}'

    
position_choices = (
    ('President', 'President'),
    ('Vice President', 'Vice President'),
    ('Secretary', 'Secretary'),
    ('Vice Secretary', 'Vice Secretary'),
    ('Treasurer', 'Treasurer'),
    ('Software Coordinator', 'Software Coordinator'),
    ('Hardware Coordinator', 'Hardware Coordinator'),
    ('Grahics Designer', 'Grahics Designer'),
    ('HR & Communications', 'HR & Communications'),
    ("Event's Manager", "Event's Manager"),
    ('Social Media Manager', 'Social Media Manager'),
)

class CommitteeMember(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    position = models.CharField(max_length=50, choices=(position_choices))
    started_from = models.DateField(null=False, blank=False)
    tenure = models.PositiveIntegerField()
    memberPhoto = models.ImageField(upload_to=member_image_path, null=True, blank=True)
    # year = models.ForeignKey(MemberTenure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Committee Member")
        verbose_name_plural = _("Committee Members")
        ordering = ['-started_from']


class SocialMedia(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(CommitteeMember, on_delete=models.CASCADE, related_name='social_media')
    platform = models.CharField(max_length=255)
    handle = models.URLField(max_length=255)

    def __str__(self):
        return str(self.user.name)+ " " +str(self.platform)
    
    

@receiver(signals.post_delete, sender=CommitteeMember)
def delete_social_media(sender, instance, **kwargs):
    # delete the image & social media of the model
    instance.memberPhoto.delete(save=False)
    instance.social_media.all().delete()
