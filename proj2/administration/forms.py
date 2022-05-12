from django import forms
from django.forms import ModelForm
from .models import Member
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserChangeForm

# Create an Item form
# class MemberForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class':'form-control'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control'},),
#             'email': forms.TextInput(attrs={'class':'form-control'}),
#         }

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['avatar']

class UserEditForm (UserChangeForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(max_length="50", required=False)
    first_name = forms.CharField(max_length="50", required=False)

    class Meta:
        model=User
        fields = ('email', 'last_name', 'first_name')
