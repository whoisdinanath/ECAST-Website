from django.db import models
import uuid

class MemberPosition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.position
    

class CommitteeMember(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    position = models.ForeignKey(MemberPosition, on_delete=models.CASCADE)
    started_from = models.DateField(null=False, blank=False)
    tenure = models.PositiveIntegerField()
    memberPhoto = models.ImageField(upload_to='member_photos/')
    # year = models.ForeignKey(MemberTenure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class SocialMedia(models.Model):
    user = models.ForeignKey(CommitteeMember, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user.name)+" " +str(self.platform)