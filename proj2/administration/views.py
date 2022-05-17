from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from pyexpat.errors import messages
from .models import Member
from .forms import MemberForm, UserEditForm, UserRegistrationForm, SelectGroupForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect



# Create your views here.
class MyListMemberView(LoginRequiredMixin, View):
    template_name = 'administration/home.html'

    def get(self, request, *args, **kwargs):
        res = Member.objects.all().order_by('pk')
        data = {
            'usr_list': res
        }

        if request.user.is_authenticated:
            group_super = Group.objects.get(name="Admin_super_grp")
            group_user = Group.objects.get(name="Admin_user_grp")
            user_to_test = request.user
            if (group_super in user_to_test.groups.all() or group_user in user_to_test.groups.all()):
                return render(request, self.template_name, context=data)
            else:
                return HttpResponseRedirect(reverse_lazy('home'))

class EditUserClassView(LoginRequiredMixin, UpdateView):
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
        this_member = Member.objects.get(user=member.user)
        member_data = {'user_pic': this_member.avatar.url}
        member_form = MemberForm(member_data)
<<<<<<< HEAD
        return render(request, self.template_name,
                      {'edit_form': edit_form, 'member_form': member_form, 'member': member.user.username})
=======

        if request.user.is_authenticated:
            group_super = Group.objects.get(name="Admin_super_grp")
            group_user = Group.objects.get(name="Admin_user_grp")
            user_to_test = request.user
            if (group_super in user_to_test.groups.all() or group_user in user_to_test.groups.all() ):
                return render(request, self.template_name,
                              {'edit_form': edit_form, 'member_form': member_form, 'member': member.user.username})
            else:
                return HttpResponseRedirect(reverse_lazy('home'))

>>>>>>> 1f830d533e51b991da59bc7087ec1d3512af43e6

    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        edit_form = UserEditForm(request.POST)
        member_form = MemberForm(request.POST, request.FILES)
        if edit_form.is_valid():
            member.user.email = edit_form.cleaned_data['email']
            member.user.last_name = edit_form.cleaned_data.get('last_name')
            member.user.first_name = edit_form.cleaned_data.get('first_name')
            if member_form.is_valid():
                member.avatar = member_form.cleaned_data.get('avatar')
                member.user.save()
                member.save()
                return HttpResponseRedirect(reverse_lazy('administration_user_list'))
        else:
            messages.error(request, f"Error occured")
            return render(request, self.template_name, {'edit_form': edit_form, 'member_form': member_form})
        return render(request, self.template_name, {'edit_form': edit_form, 'member_form': member_form})


<<<<<<< HEAD

class DeleteUserClassView(View):
=======
class DeleteUserClassView(LoginRequiredMixin, View):
>>>>>>> 1f830d533e51b991da59bc7087ec1d3512af43e6
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

        if request.user.is_authenticated:
            group_super = Group.objects.get(name="Admin_super_grp")
            group_user = Group.objects.get(name="Admin_user_grp")
            user_to_test = request.user
            if (group_super in user_to_test.groups.all() or group_user in user_to_test.groups.all() ):
                return render(request, self.template_name, {'member': member})
            else:
                return HttpResponseRedirect(reverse_lazy('home'))



    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        user = get_object_or_404(User, username=member.user.username)

        user.delete()
        member.delete()

        return HttpResponseRedirect(reverse_lazy('administration_user_list'))

<<<<<<< HEAD

class GroupUserClassView(View):
=======
class GroupUserClassView(LoginRequiredMixin, View):
>>>>>>> 1f830d533e51b991da59bc7087ec1d3512af43e6
    template_name = 'administration/member_group.html'

    def get(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        choice_form = SelectGroupForm()

<<<<<<< HEAD
        return render(request, self.template_name, {'choice_form': choice_form})


class FlagUserClassView(View):
=======
        if request.user.is_authenticated:
            group_super = Group.objects.get(name="Admin_super_grp")
            group_user = Group.objects.get(name="Admin_user_grp")
            user_to_test = request.user
            if (group_super in user_to_test.groups.all() or group_user in user_to_test.groups.all()):
                return render(request, self.template_name, {'choice_form': choice_form, 'member': member})
            else:
                return HttpResponseRedirect(reverse_lazy('home'))



    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])
        group_form = SelectGroupForm(request.POST)
        choice_form = SelectGroupForm()

        group_list = request.POST.dict()
        group_id = group_list.get('group')


        if request.user.is_authenticated:
            group_super = Group.objects.get(name="Admin_super_grp")
            group_user = Group.objects.get(name="Admin_user_grp")
            user_to_test = request.user

            if group_user in user_to_test.groups.all() and group_id == '4':
                return render(request, self.template_name, {'choice_form': choice_form, 'member': member})
            else:
                member.group = Group.objects.get(pk=group_id)
                member.user.groups.set(group_id)
                member.save()
                return HttpResponseRedirect(reverse_lazy('administration_user_list'))


class FlagUserClassView(LoginRequiredMixin, View):
>>>>>>> 1f830d533e51b991da59bc7087ec1d3512af43e6
    model = Member
    template_name = 'administration/home.html'

    def get(self, request, *args, **kwargs):
        member_flagged = get_object_or_404(Member, id=kwargs['pk'])

        if request.user.is_authenticated:
            group_super = Group.objects.get(name="Admin_super_grp")
            group_user = Group.objects.get(name="Admin_user_grp")
            user_to_test = request.user

            if (group_super in user_to_test.groups.all() or group_user in user_to_test.groups.all() ):

                if not member_flagged.is_flagged:
                    member_flagged.is_flagged = True
                else:
                    member_flagged.is_flagged = False

<<<<<<< HEAD

# class FlagUserClassView(View):
#     model = Member_Flag
#     template_name = 'administration/home.html'
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
=======
                member_flagged.save()
>>>>>>> 1f830d533e51b991da59bc7087ec1d3512af43e6

                return HttpResponseRedirect(reverse_lazy('administration_user_list'))
            else:
                return HttpResponseRedirect(reverse_lazy('home'))

class WarnUserClassView(LoginRequiredMixin, View):
    model = Member
    template_name = 'administration/home.html'

    def get(self, request, *args, **kwargs):
        member_warned = get_object_or_404(Member, id=kwargs['pk'])

        if request.user.is_authenticated:
            group_super = Group.objects.get(name="Admin_super_grp")
            group_user = Group.objects.get(name="Admin_user_grp")
            user_to_test = request.user

            if (group_super in user_to_test.groups.all() or group_user in user_to_test.groups.all() ):

                if not member_warned.is_warned:
                    member_warned.is_warned = True
                else:
                    member_warned.is_warned = False

                member_warned.save()

                return HttpResponseRedirect(reverse_lazy('administration_user_list'))
            else:
                return HttpResponseRedirect(reverse_lazy('home'))

class CreateUserClassView(LoginRequiredMixin, View):
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
                the_user.groups.set('1')
                Member.objects.create(user=the_user,
                                      avatar=avatar, group_id=1)
                return HttpResponseRedirect(reverse_lazy('administration_user_list'))
            else:
                messages.error(request, "Error occurred")
        return render(request, self.template_name, {'reg_form': reg_form})

# ---------- Rest API -----------

<<<<<<< HEAD
        return HttpResponseRedirect(reverse_lazy('administration_user_list'))
=======
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .serializer import MemberClassSerializer, UserClassSerializer

@api_view(['GET'])
@login_required()
def api_get_all_member(request):
    members = Member.objects.all()
    obj_serializer = MemberClassSerializer(members, many=True)

    if request.user.is_authenticated:
        group_super = Group.objects.get(name="Admin_super_grp")
        group_user = Group.objects.get(name="Admin_user_grp")
        user_to_test = request.user
        if (group_super in user_to_test.groups.all() or group_user in user_to_test.groups.all()):
            return Response(obj_serializer.data)
    return HttpResponseRedirect(reverse_lazy('home'))



@api_view(['GET'])
@login_required()
def api_get_all_user(request):
    users = User.objects.all()
    obj_serializer = UserClassSerializer(users, many=True)

    if request.user.is_authenticated:
        group_super = Group.objects.get(name="Admin_super_grp")
        group_user = Group.objects.get(name="Admin_user_grp")
        user_to_test = request.user
        if (group_super in user_to_test.groups.all() or group_user in user_to_test.groups.all()):
            return Response(obj_serializer.data)
    return HttpResponseRedirect(reverse_lazy('home'))
>>>>>>> 1f830d533e51b991da59bc7087ec1d3512af43e6
