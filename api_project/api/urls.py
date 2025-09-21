from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
# Create router and register our viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
     # Existing list-only endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Include all CRUD endpoints via the router
    path('', include(router.urls)),
]
