from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length = 30,primary_key=True)
    email = models.EmailField(max_length = 200)
    institution = models.CharField(max_length=70, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=25, blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username



