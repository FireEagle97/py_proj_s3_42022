from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageListView.as_view(), name="messaging_home"),
    path('messages/', views.MessageListView.as_view(), name="messaging_home"),
]
