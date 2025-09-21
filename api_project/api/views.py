from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Existing list view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Full CRUD using ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Book model:
    list, create, retrieve, update, partial_update, destroy
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
