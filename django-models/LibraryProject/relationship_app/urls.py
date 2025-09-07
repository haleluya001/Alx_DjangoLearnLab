from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    # URL for the function-based view that lists all books
    # The path is 'books/' and it maps to the 'book_list' view function.
    path('books/', book_list, name='book-list'),

    # URL for the class-based view that shows library details
    # The '<int:pk>' part is a path converter that captures a primary key
    # as an integer and passes it to the view.
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]
