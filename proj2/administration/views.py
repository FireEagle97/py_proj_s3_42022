from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from .models import Member
from .forms import MemberForm, UserEditForm, UserRegistrationForm, SelectGroupForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect


# Create your views here.
class MyListMemberView(View):
    template_name = 'administration/home.html'

    def get(self, request, *args, **kwargs):
        res = Member.objects.all().order_by('pk')
        data = {
            'usr_list': res
        }
        return render(request, self.template_name, context=data)


class EditUserClassView(UpdateView):
    form_class = UserEditForm
    success_url = reverse_lazy('administration_user_list')
    success_message = "user was updated successfully ..."
    template_name = "administration/member_edit.html"
    extra_context = {
        'form_legend': 'Update a user',
        'form_submit_btn': "Update"
    }

    def get(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])

        user_data = {'email': member.user.email,
                     'last_name': member.user.last_name,
                     'first_name': member.user.first_name}

        edit_form = UserEditForm(user_data)
        this_member = Member.objects.get(user = member.user)
        member_data = {'user_pic': this_member.avatar.url}
        member_form = MemberForm(member_data)
        return render(request, self.template_name, {'edit_form': edit_form, 'member_form': member_form, 'member': member.user.username})

    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        edit_form = UserEditForm(request.POST)
        member_form = MemberForm(request.POST, request.FILES)
        if edit_form.is_valid():
            member.user.email = edit_form.cleaned_data['email']
            member.user.last_name = edit_form.cleaned_data.get('last_name')
            member.user.first_name = edit_form.cleaned_data.get('first_name')
            member.user.save()
            return HttpResponseRedirect(reverse_lazy('administration_user_list'))
        else:
            messages.error(request, f"Error occured")
            return render(request, self.template_name, {'edit_form': edit_form, 'member_form': member_form})

class DeleteUserClassView(View):
    model = Member
    success_url = reverse_lazy('administration_user_list')
    success_message = "user was successfully deleted"
    template_name = "administration/member_delete.html"
    extra_content = {
        'form_legend': 'Delete a User',
        'form_submit_btn': "Delete"
    }

    def get(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])

        return render(request, self.template_name, {'member': member})

    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        user = get_object_or_404(User, username=member.user.username)

        user.delete()
        member.delete()

        return HttpResponseRedirect(reverse_lazy('administration_user_list'))

class GroupUserClassView(View):
    template_name = 'administration/member_group.html'

    def get(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        choice_form = SelectGroupForm()

        return render(request, self.template_name, {'choice_form': choice_form, 'member': member})

    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        group_form = SelectGroupForm(request.POST)

        group_list = request.POST.dict()
        group_id = group_list.get('group')
        member.group = Group.objects.get(pk=group_id)
        member.save()

        return HttpResponseRedirect(reverse_lazy('administration_user_list'))

class FlagUserClassView(View):
    model = Member
    template_name = 'administration/home.html'

    def get(self, request, *args, **kwargs):
        member_flagged = get_object_or_404(Member, id=kwargs['pk'])

        if not member_flagged.is_flagged:
            member_flagged.is_flagged = True
        else:
            member_flagged.is_flagged = False

        member_flagged.save()

        return HttpResponseRedirect(reverse_lazy('administration_user_list'))


class WarnUserClassView(View):
    model = Member
    template_name = 'administration/home.html'

    def get(self, request, *args, **kwargs):
        member_warned = get_object_or_404(Member, id=kwargs['pk'])

        if not member_warned.is_warned:
            member_warned.is_warned = True
        else:
            member_warned.is_warned = False

        member_warned.save()

        return HttpResponseRedirect(reverse_lazy('administration_user_list'))

class CreateUserClassView(View):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('administration_user_list')
    template_name = 'administration/member_create.html'

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
                                      avatar=avatar, group_id=1)
                return HttpResponseRedirect(reverse_lazy('administration_user_list'))
            else:
                messages.error(request, "Error occurred")
        return render(request, self.template_name, {'reg_form': reg_form})