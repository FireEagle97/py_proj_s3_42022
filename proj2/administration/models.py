from django.contrib.auth.models import User, Group
from django.db import models
from PIL import Image


group_choices = ((1, "Members"), (2, "User Admin"), (3, "Item Admin"), (4, "Super User"))
# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, choices=group_choices ,on_delete=models.CASCADE)
    is_flagged = models.BooleanField(default=False)
    is_warned = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='user_pics/',
                               default='user_default_image.png')

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)  # Open image
    #
    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)  # Resize image
    #         img.save(self.image.path)  # Save it again and override the larger image
