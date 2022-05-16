from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyListItems.as_view(), name='home'),
    path('contact', views.contact, name='itemCatalog_contact'),
    path('home/', views.MyListItems.as_view(), name='home'),
    path('item/<int:pk>', views.ItemReviewDetail.as_view(), name='itemCatalog-item-detail'),
    path('item/create/', views.CreateItemClassView.as_view(), name="itemCatalog-item-create"),
    path('item/update/<int:pk>', views.UpdateItemClassView.as_view(), name='itemCatalog-item-update'),
    path('item/delete/<int:pk>', views.DeletePostClassView.as_view(), name='itemCatalog-item-delete'),
    path('item/search/', views.ListSearchedItems.as_view(), name='itemCatalog-item-search'),
    path('ordered_alph_asc',views.OrderItemsByAlphAsc.as_view(),name='itemCatalog-item-order-asc-alph'),
    path('ordered_alph_desc',views.OrderItemsByAlphDesc.as_view(),name='itemCatalog-item-order-desc-alph'),
    path('ordered_price_desc',views.OrderItemsByPriceDesc.as_view(),name='itemCatalog-item-order-desc-price'),
    path('ordered_price_asc',views.OrderItemsByPriceAsc.as_view(),name='itemCatalog-item-order-asc-price'),
    path('like/<int:pk>', views.LikeItemView.as_view(), name='itemCatalog-likeItem'),
    path('flag/<int:pk>', views.FlagItemView.as_view(), name='itemCatalog-flagItem'),

]
