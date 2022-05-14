# Create your views here.
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from administration.models import Member
from .models import Item, Review
from .forms import ItemForm, ReviewForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class MyListItemsView(View):
    template_name = 'itemCatalog/home.html'

    def get(self, req, *args, **kwargs):
        res = Item.objects.all()
        data = {'page_title': "List Items page",
                'greet': "list Items",
                'object_list': res,
                }
        return render(req, self.template_name, context=data)


class MyItemDetail(DetailView):
    model = Item


class ItemReviewDetail(FormMixin, DetailView):
    template_name = 'itemCatalog/item_detail.html'
    model = Item
    form_class = ReviewForm

    def get(self, request, *args, **kwargs):
        the_item = get_object_or_404(Item, id=kwargs.get('pk'))
        review_form = ReviewForm
        item_reviews = Review.objects.filter(item_id=the_item.id)

        context = {
            'item': the_item,
            'review_form': review_form,
            'item_reviews': item_reviews,
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        # if not request.user.is_authenticated:
        #     return HttpResponseForbidden()
        the_item = get_object_or_404(Item, id=kwargs.get('pk'))
        review_form = ReviewForm(request.POST)
        context = {
            'item': the_item,
            'review_form': review_form,

        }
        if review_form.is_valid():
            member = Member.objects.get(user=request.user)
            Review.objects.filter(item=the_item).filter(author=member).delete()
            Review.objects.create(rate=review_form.instance.rate, item=the_item, author=member,
                                  comment=review_form.instance.comment)
            messages.success(request, 'Successfullly added a review')
            return render(request, self.template_name, context)
        else:
            messages.error(request, f'an error has occured')
            return render(request, self.template_name, context)


class MyListItems(ListView):
    model = Item


# class MyItemDetailView(View):
#     model = Item
#     template_name = 'itemCatalog/item_detail.html'
#
#     def get(self, req, **kwargs):
#         my_item = get_object_or_404(Item, id=kwargs['id'])
#         return render(req, self.template_name, {'i': my_item})


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
        item2update = self.get_object()

        print(f"res:{self.request.user == item2update.owner.user}")
        return self.request.user == item2update.owner.user


class DeletePostClassView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('home')
    success_message = "item was deleted successfully ..."

    def test_func(self):
        post2delete = self.get_object()

        print(f"res:{self.request.user == post2delete.owner.user}")
        return self.request.user == post2delete.owner.user


class ListSearchedItems(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'itemCatalog/item_search.html'

    def post(self, req):
        searched = req.POST['searched']
        items_list = Item.objects.filter(title__icontains=searched)
        if items_list.exists():
            return render(req, self.template_name, {'searched': searched,
                                                    'items_list': items_list, })
        else:
            return render(req, self.template_name, {'searched': "No results found",
                                                    })
