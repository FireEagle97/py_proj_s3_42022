from django.contrib import admin
from .models import *

all_models = (Item, Review)
admin.site.register(all_models)


# Register your models here.
# @admin.register(Item)
# class ReviewAdmin(admin.Model.Admin):
#     list_display = ['owner', 'title', 'genre', 'description', 'price', 'address', 'status', 'rate']
