from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyListMemberView.as_view(), name='administration_user_list'),
    path('user-list', views.MyListMemberView.as_view(), name='administration_user_list'),
    path('user-edit/<int:pk>', views.EditUserClassView.as_view(), name='administration_edit_user'),
    path('user-delete/<int:pk>', views.DeleteUserClassView.as_view(), name='administration_delete_user'),
    path('member-group/<int:pk>', views.GroupUserClassView.as_view(), name='administration_group_user'),
    path('member_flag/<int:pk>', views.FlagUserClassView.as_view(), name='administration_flag_user'),
    # path('user-create/', views.CreateUserClassView.as_view(), name='administration_create_user'),
]
