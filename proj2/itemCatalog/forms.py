from django import forms
from django.forms import ModelForm
from .models import Item


# Create an Item form
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'genre', 'description', 'price', 'address', 'status', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'genre': forms.TextInput(attrs={'class':'form-control'},),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control-file'}),

        }
