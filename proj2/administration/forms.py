from django import forms
from django.forms import ModelForm
from .models import Member
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserChangeForm, UserCreationForm



class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['avatar']

class UserEditForm (ModelForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(max_length="50", required=True)
    first_name = forms.CharField(max_length="50", required=True)

    class Meta:
        model=User
        fields = ('email', 'first_name', 'last_name')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(max_length="50", required=True)
    first_name = forms.CharField(max_length="50", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'last_name', 'first_name']
#
# class SelectGroupForm(ModelForm):
class SelectGroupForm(ModelForm):
    class Meta:
        model = Member
        fields = ['group']

        widgets = {
            'group': forms.Select(attrs={'class': 'form-control'}),
        }
