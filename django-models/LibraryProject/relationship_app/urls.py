from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Book views
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),               
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),   
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

    # Library view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
