from django import forms
from django.forms import ModelForm
from .models import Item


# Create an Item form
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'genre', 'description', 'price', 'address', 'status', 'image')
