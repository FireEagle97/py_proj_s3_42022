from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_pics',
                              default='user_default_image.png')

