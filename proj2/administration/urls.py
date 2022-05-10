from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyListMemberView.as_view(), name='administration_user_list'),
    path('user-list', views.MyListMemberView.as_view(), name='administration_user_list'),
    path('user-edit/<int:pk>', views.MyEditMemberDetailView.as_view(), name='administration_edit_user'),
]
