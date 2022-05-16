from django.db import models


# Create your models here.
from administration.models import Member


class Message(models.Model):
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="sender")
    #sender_id = models.IntegerField
    recipient = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="recipient")
    #recipient_id = models.IntegerField
    msg_text = models.CharField(max_length=200, help_text="Enter your message")
    send_date = models.DateTimeField("Sent on")
    # potentially use dt.now for dates upon instantiation
    unread = models.BooleanField(default=False)

    def __str__(self):
        return self.sender #+ ' | ' + self.send_date

# class MessageMenu(models.Model):
#     sender = models.CharField(max_length=100)
#     sender_id = models.IntegerField
#     send_date = models.DateTimeField("Sent on")

# class Notif(models.Model):
#     amount = models.IntegerField(default=0)


object_list = [
    (1, "user1", 2, "user2", "This is a test message", "30-04-22 15:03:24"),
    (2, "user2", 1, "user1", "This is a test reply", "30-04-22 15:13:57"),
    (1, "user1", 2, "user2", "Just got back to you a day later, my bad.", "01-01-22 7:00:00")
    # I couldn't find much on the datetimefield format, so this can be changed later
]
