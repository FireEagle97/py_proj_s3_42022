from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.

# item models
from django.db.models import CASCADE

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()


class Team(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)


class Member_Team(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
