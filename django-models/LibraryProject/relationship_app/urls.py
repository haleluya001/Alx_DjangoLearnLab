from django.urls import path
from . import views
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books


urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # FBV
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # CBV

    # Authentication
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register_view, name="register"),  # registration still custom

    # Role-based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]
