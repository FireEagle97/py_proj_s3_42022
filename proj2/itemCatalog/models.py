from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from administration.models import Member

status_Choices = (("N","New"), ("LN","Like New"), ("U","Used"))


class Item(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=status_Choices, default="New")
    rate = models.DecimalField(max_digits=3, decimal_places=0, null=True, default=0)
    image = models.ImageField(upload_to='item_pics',
                              default='item_default_image.jpg')

    def __str__(self):
        return f"{self.title[:15]}"


lst_items = [
    ("Lego Star Wars", "Video Game", "Lego Star Wars: The Complete Saga is\
                                                      a Lego-themed action-adventure video game based on the Lego Star Wars line of toys.\
                                                      It is a combination of the game Lego Star Wars: The Video Game and its sequel Lego Star Wars II:\
                                                      The Original Trilogy, which spans the first six episodes of the Star Wars saga.",
     "24.99", "123 Boardwalk Avernue", "New", "87"),
    ("Dune", "Book", "Dune is a 1965 epic science fiction novel by American author Frank Herbert,\
                    originally published as two separate serials in Analog magazine.\
                    It tied with Roger Zelazny's This Immortal for the Hugo Award in 1966 and it won the inaugural Nebula Award for Best Novel.\
                    It is the first installment of the Dune saga.",
     "19.99", "55 Irakis Road", "New", "82"),
    ("Wood Desk", "Furniture", "A 1988 Antique Wood Desk", "499.99", "99 Forest Avenue", "Used", "92"),

]
