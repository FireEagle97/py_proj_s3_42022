from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from proj2.user_management.forms import UserRegistrationForm

# Create your views here.

from .forms import UserRegistrationForm


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse('user_management_register')
    template_name = 'user_management/register'

    def get(self, request, *args, **kwargs):
        reg_form = UserRegistrationForm()
        return render(request, self.template_name,
                      {'reg_form': reg_form})

    def post(self, request, *args, **kwargs):
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data.get('username')
            reg_form.save()
            if not member_form.is_valid():
                raise ValueError(f" error with pic uplaod ...")
            else:
                user_pic = member_form.cleaned_data.get('user_pic')
                the_user = User.objects.get(username=username)
                Member.objects.create(affiliation=affiliation, user=the_user,
                                      user_pic=user_pic)
                messages.success(request, f"Accout successfuly created fro {username}")
                return redirect('member_login')



# def home(req):
#     template_name='user_management/home.html'
#     print (f"req.user.username {req.user.username}")
#     amember = Member.objects.get(user__username = req.user.username)
#     context = {'amember': amember}
#
#     return render (req, template_name, context)

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


# def register(request):
#     if request.method == "POST":
#         print(f"type post {type(request.POST)}")
#         reg_form = UserRegistrationForm(request.POST)
#         if reg_form.is_valid():
#             username = reg_form.cleaned_data.get('username')
#             reg_form.save()  # save user data (username, pass, email., ...
#             return redirect('member_login')
#         else:
#             messages.error(request, f"some error while creating account")
#     else:
#         reg_form = UserRegistrationForm()
#     return render(request, 'user_management/register.html', {'reg_form': reg_form})

# def register(request):
#     template_name = 'member/register.html'
#     if request.method == "POST":
#         print(f"type post {type(request.POST)}")
#         reg_form = UserRegistrationForm(request.POST)
#
#         if reg_form.is_valid():
#             username = reg_form.cleaned_data.get('username')
#             reg_form.save()  # save user data (username, pass, email., ...
#             if not member_form.is_valid():
#                 raise ValueError(f" error with pic uplaod ...")
#             else:
#                 affiliation = member_form.cleaned_data.get('affiliation')
#                 user_pic = member_form.cleaned_data.get('user_pic')
#                 the_user = User.objects.get(username=username)
#                 Member.objects.create(affiliation=affiliation, user=the_user,
#                                       user_pic=user_pic)
#                 messages.success(request, f"Accout successfuly created fro {username}")
#                 return redirect('member_login')
#         else:
#             messages.error(request, f"some error while creating account")
#     else:
#         reg_form = UserRegistrationForm()
#         member_form = MemberForm()
#
#     return render(request, template_name, {'reg_form': reg_form, 'member_form': member_form})
