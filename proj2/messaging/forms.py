from django import forms
from django.forms import ModelForm
from .models import Message


# Create an Item form
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ()
        # fields = ('recipient_id', 'msg_text')