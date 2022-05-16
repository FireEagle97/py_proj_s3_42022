from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Message
from .forms import MessageForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

# A view of the list of people who have sent you messages
class MessageListView(ListView):
    template_name = 'messaging/home.html'
    model = Message

    def get(self, req, *args, **kwargs):
        res = Message.objects.all()
        data = {
            'page_title': "Message List",
            'greet': "Lists Messages sent to you.",
            'object_list': res
        }
        print(data)
        return render(req, self.template_name, context=data)


# After clicking on somebody on the page, a view of messages between each other
class FullMessageView(ListView):
    model = Message


class CreateMessageClassView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('home')
    success_message = "item was created successfully ..."
    extra_context = {
        'form_legend': 'Create a New Item',
        'form_submit_btn': "NEW Item!"
    }
