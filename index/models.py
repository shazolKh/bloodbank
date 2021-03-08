from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    location = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    managed = models.CharField(max_length=5, blank=True, default='No')
    details = models.TextField()
    date = models.DateField(default=date.today, blank=True)

    def __str__(self):
        return f'Post of {self.user.first_name}'


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return f"{self.user.first_name}'s Testimonial"
