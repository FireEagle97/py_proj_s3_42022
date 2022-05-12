from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from administration.models import Member
from .models import Message, MessageMenu
from .forms import MessageForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

# A view of the list of people who have sent you messages
class MessageListView(View):
    template_name = 'home.html'
    model = MessageMenu

    def get(self, req, *args, **kwargs):
        res = Message.objects.all()
        data = {
            'page_title': "Message List",
            'greet': "Lists Messages sent to you.",
            'object_list': res
        }
        return render(req, self.template_name, context=data)


# After clicking on somebody on the page, a view of messages between each other
class PrivateMessageView(ListView):
    model = Message
