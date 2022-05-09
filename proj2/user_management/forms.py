from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(max_length="50", required=True)
    first_name = forms.CharField(max_length="50", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'last_name', 'first_name']


from ..administration.models import Member

class MemberForm (forms.ModelForm):
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


