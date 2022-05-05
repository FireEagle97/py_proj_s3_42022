from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item_list', views.MyListItemsView.as_view(), name='item_list'),
    path('home', views.home, name='home'),
    path('item/<int:pk>', views.MyItemDetail.as_view(), name='itemCatalog_item_detail'),
    path('add_item', views.add_item, name="add_item"),

]
