from django.db import models


class MemberPosition(models.Model):
    position = models.CharField(max_length=50, choices=[('Software Team', 'Software Team'),
                                                        ('Hardware Team', 'Hardware Team'),
                                                        ('Secretary', 'Secretary'),
                                                        ('President', 'President'),
                                                        ('Vice President', 'Vice President'),
                                                        ('Graphics Designer', 'Graphics Designer'),
                                                        ('Social Media Manager/Communication', 'Social Media Manager/Communication'),
                                                        ('Research and Development', 'Research and Development'),
                                                        ('Hardware Coordinator', 'Hardware Coordinator'),
                                                        ('Software Coordinator', 'Software Coordinator')])
    

    def __str__(self):
        return self.position
    


class MemberTenure(models.Model):
    year = models.PositiveIntegerField(choices=[(2076, 2076),
                                                (2077, 2077),
                                                (2078, 2078),
                                                (2079, 2079),
                                                (2080, 2080)])

    def __str__(self):
        return str(self.year)



class CommitteeMembers(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.ForeignKey(MemberPosition, on_delete=models.CASCADE)
    socialMedia = models.URLField(blank=True)
    memberPhoto = models.ImageField(upload_to='media/member_photos/')
    year = models.ForeignKey(MemberTenure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

