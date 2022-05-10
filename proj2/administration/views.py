from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from .models import Member
from .forms import MemberForm

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

class MyEditMemberDetailView(FormView):
    model = Member
    template_name = 'administration/user_edit.html'
    form_class = MemberForm

    def get(self, request, *args, **kwargs):
        member = get_object_or_404(Member, id=kwargs['pk'])

        return render(request, self.template_name, {'member': member})

# class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin,
#                           UserPassesTestMixin, UpdateView):
#     model = Member
#     fields = ('title', 'body')
#     success_url = reverse_lazy('weblog_list_all')
#     success_message = "You justr updated a post!"
#     extra_context = {
#         'for_toitl': "Update USING CBV",
#         'btn_val': "Update PPPOST"
#     }
#
#     def test_func(self):
#         current_user = self.get_object()
#         return self.request.user == current_user.user
