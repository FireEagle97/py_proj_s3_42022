from django.db import models


# Create your models here.

# item models
from django.db.models import CASCADE





# user/group models
from proj2.item_catalog.models import Item


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    # avatar = models.


class Group(models.Model):
    group_name = models.CharField(max_length=20)


class User_Group(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    group = models.ForeignKey(Group, on_delete=CASCADE)


# post-related models

class Comment(models.Model):
    commenter_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ForeignKey(Item, on_delete=CASCADE)
    rating = models.IntegerField(max_digits=3)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ForeignKey(Item, on_delete=CASCADE)
    #liked = models.Booleanfield()


# flag models

class Item_Flag(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ForeignKey(Item, on_delete=CASCADE)


class User_Flag(models.Model):
    flagger = models.ForeignKey(User, on_delete=CASCADE)
    flagged = models.ForeignKey(User, on_delete=CASCADE)


# message models

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=CASCADE)
    sent = models.ForeignKey(User, on_delete=CASCADE)
    content = models.CharField(max_length=200)
    is_seen = models.BooleanField()
