from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from user_management.forms import UserRegistrationForm, MemberForm, UserEditForm

# Create your views here.

from .forms import UserRegistrationForm
from administration.models import Member


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user_management_register')
    template_name = 'user_management/register.html'

    def get(self, request, *args, **kwargs):
        reg_form = UserRegistrationForm()
        member_form = MemberForm()
        return render(request, self.template_name,
                      {'reg_form': reg_form, 'member_form': member_form})

    def post(self, request, *args, **kwargs):
        reg_form = UserRegistrationForm(request.POST)
        member_form = MemberForm(request.POST, request.FILES)
        if reg_form.is_valid():
            username = reg_form.cleaned_data.get('username')
            reg_form.save()
            if member_form.is_valid():
                avatar = member_form.cleaned_data.get('avatar')
                the_user = User.objects.get(username=username)
                Member.objects.create(user=the_user,
                                      avatar=avatar)
                messages.success(request, "Account successfully created for {username}")
                return redirect('member_login')
            else:
                messages.error(request, "Error occurred")
        return render(request, self.template_name, {'reg_form': reg_form})


class EditView(UpdateView):
    form_class = UserEditForm
    success_url = reverse_lazy('user_management_home')  # change to home
    template_name = 'user_management/edit.html'

    def get(self, request, *args, **kwargs):
        user_data = {'email': request.user.email,
                     'last_name': request.user.last_name,
                     'first_name': request.user.first_name}
        edit_form = UserEditForm(user_data)
        this_member = Member.objects.get(user=request.user)
        member_data = {'avatar': this_member.avatar.url}
        member_form = MemberForm(member_data)
        return render(request, self.template_name,
                      {'edit_form': edit_form, 'member_form': member_form})

    def post(self, request, *args, **kwargs):
        edit_form = UserEditForm(request.POST)
        member_form = MemberForm(request.POST, request.FILES)
        if edit_form.is_valid():
            email = edit_form.cleaned_data['email']
            last_name = edit_form.cleaned_data['last_name']
            first_name = edit_form.cleaned_data['first_name']
            request.user.email = email
            request.user.last_name = last_name
            request.user.first_name = first_name
            request.user.save()
            edit_form.save()
            if member_form.is_valid():
                avatar = member_form.cleaned_data.get('avatar')
                this_member = Member.objects.get(user=request.user)
                this_member.avatar = avatar
                this_member.save()
                member_form.save()
                messages.success(request, "Profile updated")
                return redirect('member_login')
            else:
                messages.error(request, "Error occurred")
        return render(request, self.template_name, {'edit_form': edit_form, 'member_form': member_form})
