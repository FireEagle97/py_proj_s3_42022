# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Item
from django.http import HttpResponseRedirect
from .forms import ItemForm


def home(req):
    data = {'page_title': "Docs App",
            'greet': "Welcome to Home Page"}
    return render(req, 'itemCatalog/home.html', context=data)


def item_list(req):
    data = {'page_title': "Docs App",
            'greet': "Welcome to Home Page"}
    return render(req, 'itemCatalog/items_list.html', context=data)


class MyListItemsView(View):
    template_name = 'itemCatalog/items_list.html'

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


def add_item(req):
    submitted = False
    if req.method == "POST":
        form = ItemForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_item?submitted=True')
    else:
        form = ItemForm
        if 'submitted' in req.GET:
            submitted=True
    form = ItemForm
    return render(req, 'itemCatalog/add_item.html', {'form':form, 'submitted':submitted})
