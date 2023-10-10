from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    repo_link = models.URLField(max_length=255)
    live_link = models.URLField(max_length=255, null=True, blank=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ['-featured']
