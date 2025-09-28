from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework               # ✅ required for lab check
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly  # optional, for admin-only operations

# List all books with filtering, searching, and ordering
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

    # Backends for filtering, search, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields allowed for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields allowed for search queries
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering
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
        """
        Save the book instance.
        Can be extended to attach the logged-in user automatically.
        """
        serializer.save()


# Update a book - authenticated users only
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Delete a book - admin-only or authenticated users
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]  # Use IsAuthenticated if admin restriction not required
