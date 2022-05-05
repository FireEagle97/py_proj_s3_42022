from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from project2.proj2.user_management.forms import UserRegistrationForm


# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username = username, password = password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})


def register(request):
    template_name = 'member/register.html'
    if request.method == "POST":
        print(f"type post {type(request.POST)}")
        reg_form = UserRegistrationForm(request.POST)

        if reg_form.is_valid():
            username = reg_form.cleaned_data.get('username')
            reg_form.save()  # save user data (username, pass, email., ...

            return redirect('member_login')
        else:
            messages.error(request, f"some error while creating account")
    else:
        reg_form = UserRegistrationForm()

    return render(request, template_name, {'reg_form': reg_form})
