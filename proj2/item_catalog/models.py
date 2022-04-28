from django.db import models


# Create your models here.
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
