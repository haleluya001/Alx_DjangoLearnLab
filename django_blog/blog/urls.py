# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('', views.home_view, name='home'),
    # Login using built-in auth view
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    # Logout using built-in auth view
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
