import os
import random
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
def photo_path(instance, filename):
    base_name, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for x in range(15))
    return 'profile/{userid}_{randomstring}{ext}'.format(userid=instance.user.id, basename=base_name,
                                                         randomstring=random_str, ext=file_extension)


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
    dp = models.ImageField(default='profile/default.png', upload_to=photo_path, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
