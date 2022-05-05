from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Member

# Create your views here.
def home(req):
    template_name = 'administration/home.html'
    return render(req, template_name)


class MyListMemberView(View):
    template_name = 'administration/user_list.html'

    def get(self, request, *args, **kwargs):
        res = Member.objects.all()
        data = {
            'usr_list': res
        }
        return render(request, self.template_name, context=data)

class MyEditMemberDetailView(View):
    model = Member
    template_name = 'administration/user_detail.html'

    def get(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['id'])

        return render(request, self.template_name, {'member': member})

class MyModifyTeamView(View):
    model = Member
    template_name = 'administration/user_group.html'

    def get(self, request, *args, **kwargs):
        team = get_object_or_404()