from django.db import models
import re

# Create your models here.

def verify_roll(roll):
    # THA<0-9><0-9><0-9><B**><0-9><0-9><0-9>
    pattern = re.compile(r'^THA\d{3}B\d{2}$')
    return pattern.match(roll)

department_choices = [

    ('BCT', 'Computer Engineering'),
    ('BCE', 'Civil Engineering'),
    ('BEL', 'Electrical Engineering'),
    ('BEI', 'Electronics, Communication and Information Engineering'),
    ('BME', 'Mechanical Engineering'),
    ('BIE', 'Industrial Engineering'),
    ('BAM', 'Automobile Engineering'),
]

batch_choices = [

    ('75', '2075'),
    ('76', '2076'),
    ('77', '2077'),
    ('78', '2078'),
    ('79', '2079'),
    ('80', '2080'),
    ('81', '2081'),
]

def file_validator(file):
    if file.size > 5*1024*1024:
        raise ValidationError('File size should be less than 5MB')
    if file.name.split('.')[-1] not in ['pdf']:
        raise ValidationError('Only pdf files are allowed')



post_choices=[
        ('TT', 'Technical Team'),
        ('RD', 'Research & Development'),
        ('SMM', 'Social Media Manager'),
        ('EC', 'Events & Communication'),
        ('EIC', 'Editor in Chief'),
        ('GD', 'Graphics Designer'),
    ] 


class IntakeForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    campus_roll = models.CharField(max_length=10, validators=[verify_roll])
    department = models.CharField(max_length=100, choices=department_choices)
    batch = models.CharField(max_length=10, choices=batch_choices)
    post = models.CharField(max_length=100, choices=post_choices)
    about = models.TextField()
    reason_to_join = models.TextField()
    interests = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    filled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Intake Form'
        verbose_name_plural = 'Intake Forms'
        ordering = ['-filled_date']