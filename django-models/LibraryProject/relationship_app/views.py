from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Step 1: Implement a Function-based View
def book_list(request):
    """
    A function-based view that lists all books.
    This view fetches all Book objects from the database and passes them
    to the 'book_list.html' template for rendering.
    """
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'relationship_app/book_list.html', context)

# Step 2: Implement a Class-based View
class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library.
    It uses Django's built-in DetailView to handle the retrieval of a
    single object by its primary key (pk).
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
