from django.db import models


class MemberPosition(models.Model):
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.position
    


class MemberTenure(models.Model):
    year = models.PositiveIntegerField()

    def __str__(self):
        return str(self.year)
    
    

class CommitteeMember(models.Model):

    name = models.CharField(max_length=50, unique=True)
    position = models.ForeignKey(MemberPosition, on_delete=models.CASCADE)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    memberPhoto = models.ImageField(upload_to='member_photos/')
    year = models.ForeignKey(MemberTenure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

