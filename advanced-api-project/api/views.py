from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly 


#  List all books
class BookCreateView(generics.CreateAPIView):
    """
    Handles POST requests to create a new book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom behavior when creating a book.
        Right now, it just saves the book normally,
        but you could extend this to:
        - attach the logged-in user automatically,
        - enforce extra rules,
        - or log the creation event.
        """
        serializer.save()

# Retrieve a single book by ID

class BookListView(generics.ListAPIView):
    """
    Handles GET requests to list all books.
    Allows read-only access to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    Handles GET requests for a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


#  Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    Handles POST requests to create a new book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


#  Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Handles PUT/PATCH requests to update an existing book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


#  Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Handles DELETE requests to remove a book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
