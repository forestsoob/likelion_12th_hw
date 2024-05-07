from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    body = models.TextField()
    pub_date = models.DateTimeField()


    def __str__(self):
        return self.title