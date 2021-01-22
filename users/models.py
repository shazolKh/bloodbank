from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=3)
    blood_group = models.CharField(max_length=5)
    weight = models.CharField(max_length=10)
    gender = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    mobile2 = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    disease = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'
