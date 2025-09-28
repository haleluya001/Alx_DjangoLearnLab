from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly  

from django_filters.rest_framework import DjangoFilterBackend



class BookListView(generics.ListAPIView):
    """
    Lists all books with filtering, search, and ordering capabilities.
    - Filtering: title, author, publication_year
    - Searching: title, author
    - Ordering: title, publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #  Backends for filtering, search, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    #  Fields allowed for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    #  Fields allowed for search queries
    search_fields = ['title', 'author__name']  # author__name for related model field

    #  Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']

    # Optional: default ordering
    ordering = ['title']


# Retrieve a single book - read-only for anyone
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book - authenticated users only
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# Update a book - authenticated users only
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete a book - authenticated users only (or admin-only if you prefer)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # or [IsAdminOrReadOnly] for admin-only
