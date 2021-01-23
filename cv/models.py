from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100, default='Job Seeker')
    nationality = models.CharField(max_length=50)
    language = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    certificates = models.TextField()
    address_one = models.CharField(max_length=50)
    address_two = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/profile', blank=True, null=True)


    def __str__(self):
        return self.name