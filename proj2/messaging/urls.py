from django.urls import path
from . import views
from .views import MessageListView

urlpatterns = [
    path('', MessageListView.as_view(), name="home")
]
