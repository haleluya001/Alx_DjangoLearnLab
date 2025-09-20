from django.contrib import admin
from .models import Book

# Custom admin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in list view
    search_fields = ('title', 'author')                      # Search bar
    list_filter = ('publication_year',)                     # Sidebar filters
    ordering = ('title',)                                    # Optional ordering

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)
