from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    summary = models.TextField()
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    experience = models.TextField()
    skills = models.TextField()


    def __str__(self):
        return self.name