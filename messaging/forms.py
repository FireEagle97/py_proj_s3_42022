from django import forms
from django.forms import ModelForm
from .models import Message


# Create an Item form
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('recipient', 'msg_text')
