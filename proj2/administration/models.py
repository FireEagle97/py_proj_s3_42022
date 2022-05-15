from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_flagged = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='user_pics',
                              default='user_default_image.png')


class Member_Warn(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    is_warned = models.BooleanField()