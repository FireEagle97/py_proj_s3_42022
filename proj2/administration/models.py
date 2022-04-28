from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.

# item models
from django.db.models import CASCADE

# user/group models
class Item(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=3, decimal_places=0)
    image = models.ImageField(upload_to='user_pics',
                                     default='default_image.png')

    def __str__(self):
        return f"{self.title[:15]}"



class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()


class Team(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)


class Member_Team(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


# post-related models

class Comment(models.Model):
    commenter_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)


class Rating(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=3, decimal_places=0)


class Like(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # liked = models.Booleanfield()


# flag models

class Item_Flag(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


# class User_Flag(models.Model):
#     flagger = models.ForeignKey(Member, on_delete=models.CASCADE)
#     flagged = models.ForeignKey(Member, on_delete=models.CASCADE)
#
#
# # message models
#
# class Message(models.Model):
#     sender = models.ForeignKey(Member, on_delete=models.CASCADE)
#     sent = models.ForeignKey(Member, on_delete=models.CASCADE)
#     content = models.CharField(max_length=200)
#     is_seen = models.BooleanField()
