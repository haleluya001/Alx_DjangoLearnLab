from django.views.generic import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library  # adjust if your models are in bookshelf

# Function-based view

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"