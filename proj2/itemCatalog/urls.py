from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyListItems.as_view(), name='home'),
    path('home/', views.MyListItems.as_view(), name='home'),
    path('item/<int:pk>', views.ItemReviewDetail.as_view(), name='itemCatalog_item_detail'),
    path('item/create/', views.CreateItemClassView.as_view(), name="item-create"),
    path('item/update/<int:pk>', views.UpdateItemClassView.as_view(), name='item-update'),
    path('item/delete/<int:pk>', views.DeletePostClassView.as_view(), name='item-delete'),
    path('item/search/', views.ListSearchedItems.as_view(), name='item_search'),
    path('ordered_alph_asc',views.OrderItemsByAlphAsc.as_view(),name='item_order_asc_alph'),
    path('ordered_alph_desc',views.OrderItemsByAlphDesc.as_view(),name='item_order_desc_alph'),
    path('ordered_price_desc',views.OrderItemsByPriceDesc.as_view(),name='item_order_desc_price'),
    path('ordered_price_asc',views.OrderItemsByPriceAsc.as_view(),name='item_order_asc_price'),

# ------ Rest API paths ----
    path('api/item-list', views.api_get_all_item, name='api_item_list'),
    path('api/review-list', views.api_get_all_review, name='api_review_list'),
    path('api/item-new', views.api_create_item, name='api_item_new'),
]
