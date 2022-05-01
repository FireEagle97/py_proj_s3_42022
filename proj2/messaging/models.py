from django.db import models


# Create your models here.
class Message(models.Model):
    msg_text = models.CharField(max_length=200, help_text="Enter your message")
    send_date = models.DateTimeField("Sent on")
    # potentially use dt.now for dates upon instantiation
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    unread = models.BooleanField(default=False)


class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    sender = models.CharField(max_length=100)
    send_date = models.DateTimeField("Sent on")


class Notif(models.Model):
    amount = models.IntegerField(default=0)
