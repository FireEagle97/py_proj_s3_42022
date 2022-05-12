from django import forms
from django.forms import ModelForm
from .models import Message


# Create an Item form
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('sender', 'sender_id', 'recipient', 'recipient_id', 'msg_text', 'send_date', 'undread')

        widgets = {

        }