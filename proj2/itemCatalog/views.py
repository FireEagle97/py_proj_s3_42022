# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from administration.models import Member
from .models import Item
from .forms import ItemForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class MyListItemsView(View):
    template_name = 'itemCatalog/item_list.html'

    def get(self, req, *args, **kwargs):
        res = Item.objects.all()
        data = {'page_title': "List Items page",
                'greet': "list Items",
                'object_list': res,
                }
        return render(req, self.template_name, context=data)


class MyItemDetail(DetailView):
    model = Item


class MyListItems(ListView):
    model = Item


class MyItemDetailView(View):
    model = Item
    template_name = 'itemCatalog/item_detail.html'

    def get(self, req, *args, **kwargs):
        my_item = get_object_or_404(Item, id=kwargs['id'])
        return render(req, self.template_name, {'i': my_item})


class CreateItemClassView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('home')
    success_message = "item was created successfully ..."
    extra_context = {
        'form_legend': 'Create a New Item',
        'form_submit_btn': "NEW Item!"
    }

    def form_valid(self, form):
        form.instance.owner = \
            Member.objects.get(user=self.request.user)
        return super().form_valid(form)


class UpdateItemClassView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('home')
    success_message = "item was updated successfully ..."
    extra_context = {
        'form_legend': 'Update an item',
        'form_submit_btn': "Update"
    }

    def test_func(self):
        post2update = self.get_object()

        print(f"res:{self.request.user == post2update.owner.user}")
        return self.request.user == post2update.owner.user


class DeletePostClassView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('home')
    success_message = "item was deleted successfully ..."

    def test_func(self):
        post2delete = self.get_object()

        print(f"res:{self.request.user == post2delete.owner.user}")
        return self.request.user == post2delete.owner.user
