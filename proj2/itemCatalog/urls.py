from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyListItemsView.as_view(), name='home'),
    path('home/', views.MyListItemsView.as_view(), name='home'),
    path('item/<int:pk>', views.ItemReviewDetail.as_view(), name='itemCatalog_item_detail'),
    path('item/create/', views.CreateItemClassView.as_view(), name="item-create"),
    path('item/update/<int:pk>', views.UpdateItemClassView.as_view(), name='item-update'),
    path('item/delete/<int:pk>', views.DeletePostClassView.as_view(), name='item-delete'),
    path('item/search/', views.ListSearchedItems.as_view(), name='item_search'),

]
