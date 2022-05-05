from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyListItemsView.as_view(), name='home'),
    path('items_list', views.MyListItemsView.as_view(), name='items_list'),
    path('home/', views.MyListItemsView.as_view(), name='home'),
    path('item/<int:pk>', views.MyItemDetail.as_view(), name='itemCatalog_item_detail'),
    path('add_item', views.add_item, name="add_item"),
    path('update_item/<item_id>',views.update_item, name='update_item'),
    path('delete_item/<item_id>',views.delete_item,name='delete_item'),

]
