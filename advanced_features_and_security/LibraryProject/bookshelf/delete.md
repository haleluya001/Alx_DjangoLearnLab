# Delete Operation for Book Model

```python
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
all_books = Book.objects.all()
print(all_books)

# Expected Output:
# <QuerySet []>
