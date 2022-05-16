from django.contrib.auth.models import User, Group
from django.db import models

group_choices = ((1, "Members"), (2, "User Admin"), (3, "Item Admin"), (4, "Super User"))
# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, choices=group_choices ,on_delete=models.CASCADE)
    is_flagged = models.BooleanField(default=False)
    is_warned = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='user_pics',
                               default='user_default_image.png')
