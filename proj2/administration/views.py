from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from .models import Member
from .forms import MemberForm, UserEditForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group


# Create your views here.
def home(req):
    template_name = 'administration/home.html'
    return render(req, template_name)


class MyListMemberView(View):
    template_name = 'administration/home.html'

    def get(self, request, *args, **kwargs):
        res = Member.objects.all()
        data = {
            'usr_list': res
        }
        return render(request, self.template_name, context=data)

# class MyEditMemberDetailView(FormView):
#     model = Member
#     template_name = 'administration/user_edit.html'
#     form_class = MemberForm
#
#     def get(self, request, *args, **kwargs):
#         member = get_object_or_404(Member, id=kwargs['pk'])
#
#         return render(request, self.template_name, {'member': member})

class CreateUserClassView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('administration_user_list')
    success_message = "user was created successfully ..."
    extra_context = {
        'form_legend': 'Create a New User',
        'form_submit_btn': "Create User"
    }

    def form_valid(self, form):
        form.instance.owner = \
            Member.objects.get(user=self.request.user)
        return super().form_valid(form)


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
        return render(request, self.template_name, {'edit_form': edit_form, 'member_form': member_form})

    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        edit_form = UserEditForm(request.POST)
        member_form = MemberForm(request.POST, request.FILES)
        if edit_form.is_valid():
            member.user.email = edit_form.cleaned_data['email']
            member.user.last_name = edit_form.cleaned_data.get('last_name')
            member.user.first_name = edit_form.cleaned_data.get('first_name')
            member.user.save()
        else:
            messages.error(request, f"Error occured")
        return render(request, self.template_name, {'edit_form': edit_form, 'member_form': member_form})







class DeleteUserClassView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('administration_user_list')
    success_message = "user was successfully deleted ..."

    def test_func(self):
        user_delete = self.get_object()

        print(f"res:{1 == 1}")
        return 1 == 1


class GroupUserClassView(View):
    template_name = 'administration/user_group.html'

    def get(self, request, *args, **kwargs):
        res = Member.objects.all()
        data = {
            'usr_list': res
        }
        return render(request, self.template_name, context=data)
