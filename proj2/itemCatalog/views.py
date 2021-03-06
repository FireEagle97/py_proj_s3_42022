# Create your views here.
from abc import ABC

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
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


class MyItemDetail(DetailView):
    model = Item


class LikeItemView(View):
    model = Item

    def get(self, request, *args, **kwargs):
        item_like = get_object_or_404(Item, id=kwargs['pk'])
        if not item_like.is_liked:
            item_like.is_liked = True

        else:
            item_like.is_liked = False

        item_like.save()
        return HttpResponseRedirect(reverse_lazy('home'))


class FlagItemView(View):
    model = Item

    def get(self, request, *args, **kwargs):
        item_flag = get_object_or_404(Item, id=kwargs['pk'])
        if not item_flag.is_flagged:
            item_flag.is_flagged = True

        else:
            item_flag.is_flagged = False

        item_flag.save()
        return HttpResponseRedirect(reverse_lazy('home'))


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
            'item_flag_text': "flag",
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
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
    template_name = 'itemCatalog/item_list.html'
    ordering = ['id']
    paginate_by = 8


class OrderItemsByAlphDesc(ListView):
    model = Item
    template_name = 'itemCatalog/item_list.html'
    paginate_by = 8
    ordering = ['title']


class OrderItemsByAlphAsc(ListView):
    model = Item
    template_name = 'itemCatalog/item_list.html'
    paginate_by = 8
    ordering = ['-title']


class OrderItemsByPriceDesc(ListView):
    model = Item
    template_name = 'itemCatalog/item_list.html'
    paginate_by = 8
    ordering = ['price']


class OrderItemsByPriceAsc(ListView):
    model = Item
    template_name = 'itemCatalog/item_list.html'
    paginate_by = 8
    ordering = ['-price']


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


def contact(req):
    data = {'page_title': "Contact page",
            'greet': "Contact Info Page",
            }
    return render(req, 'itemCatalog/contact.html', context=data)
# -------- Rest API ----------------

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .serializer import ReviewClassSerializer, ItemClassSerializer

@api_view(['GET'])
@login_required()
def api_get_all_item(request):
    items = Item.objects.all()
    obj_serializer = ItemClassSerializer(items, many=True)

    return Response(obj_serializer.data)

@api_view(['POST'])
@login_required()
def api_create_item(request):
    obj_serializer = ItemClassSerializer(data=request.data)
    if obj_serializer.is_valid():
        obj_serializer.save()
        return Response(obj_serializer.data, status=status.HTTP_201_CREATED)
    return Response(obj_serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@login_required()
def api_get_all_review(request):
    reviews = Review.objects.all()
    obj_serializer = ReviewClassSerializer(reviews, many=True)

    return Response(obj_serializer.data)

