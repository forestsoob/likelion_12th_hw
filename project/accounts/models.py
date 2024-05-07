from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='account_profile', on_delete=models.CASCADE)
    department = models.TextField(null=True, max_length=30)
    hobby = models.TextField(null=True, max_length=20)