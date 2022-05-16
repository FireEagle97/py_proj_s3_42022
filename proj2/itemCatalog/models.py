from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from administration.models import Member

status_Choices = (("New", "New"), ("Like New", "Like New"), ("Used", "Used"))


class Item(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=status_Choices, default="New")
    image = models.ImageField(upload_to='item_pics/',
                              default='item_default_image.jpg')
    is_liked = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title[:15]}"


class Review(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    comment = models.TextField(max_length=250, default='')
    created_date = models.DateTimeField(auto_now_add=True)


