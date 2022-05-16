from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from .models import Member
from .forms import MemberForm, UserEditForm, UserRegistrationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect


# Create your views here.
def home(req):
    template_name = 'administration/item_list.html'
    return render(req, template_name)


class MyListMemberView(View):
    template_name = 'administration/item_list.html'

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


        return render(request, self.template_name, {'choice_form': choice_form})

class FlagUserClassView(View):
    model = Member
    template_name = 'administration/item_list.html'

    def get(self, request, *args, **kwargs):
        member_flagged = get_object_or_404(Member, id=kwargs['pk'])

        if not member_flagged.is_flagged:
            member_flagged.is_flagged = True
        else:
            member_flagged.is_flagged = False

        member_flagged.save()

        return HttpResponseRedirect(reverse_lazy('administration_user_list'))

# class FlagUserClassView(View):
#     model = Member_Flag
#     template_name = 'administration/item_list.html'
#
#     def get(self, request, *args, **kwargs):
#         member_flagged = get_object_or_404(Member, id=kwargs['pk'])
#         member_flag_count = Member_Flag.objects.filter(member=member_flagged).count()
#
#         if member_flag_count:
#             member_flag = get_object_or_404(Member_Flag, member=member_flagged)
#             if not member_flag.is_flagged:
#                 member_flag.is_flagged = True
#             else:
#                 member_flag.is_flagged = False
#         else:
#             member_flag = Member_Flag(member=member_flagged, is_flagged=True)
#         member_flag.save()
#
#         return HttpResponseRedirect(reverse_lazy('administration_user_list'))


class WarnUserClassView(View):
    model = Member
    success_url = reverse_lazy('administration_user_list')
    success_message = "user was successfully deleted"
    template_name = "administration/member_delete.html"
    extra_content = {
        'form_legend': 'Delete a User',
        'form_submit_btn': "Delete"
    }

    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        user = get_object_or_404(User, username=member.user.username)

        user.delete()
        member.delete()

        return HttpResponseRedirect(reverse_lazy('administration_user_list'))