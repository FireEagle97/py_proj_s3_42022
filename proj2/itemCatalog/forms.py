from django import forms
from django.forms import ModelForm
from .models import Item


# Create an Item form
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'genre', 'description', 'price', 'address', 'status', 'image')
        labels = {
            'title': '',
            'genre': '',
            'description': '',
            'price': '',
            'address': '',
            'status': '',
            'image': '',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'title'}),
            'genre': forms.TextInput(attrs={'class':'form-control','placeholder':'genre'},),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'description'}),
            'price': forms.NumberInput(attrs={'class':'form-control','placeholder':'price'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'address'}),
            'status': forms.NumberInput(attrs={'class':'form-control','placeholder':'status'}),
            'image': forms.FileInput(attrs={'class':'form-control','placeholder':'image'}),

        }
