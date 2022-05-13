from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='user_management_home'),
    # path('home', views.home, name='user_management_home'),
    path('login', LoginView.as_view(template_name="user_management/login.html"),
         name='member_login'),
    path('logout', LogoutView.as_view(template_name="user_management/logout.html"),
         name='member_logout'),
    path('register', views.RegisterView.as_view(), name='member_register'),
    path('edit', views.EditView.as_view(), name='member_edit'),

]
