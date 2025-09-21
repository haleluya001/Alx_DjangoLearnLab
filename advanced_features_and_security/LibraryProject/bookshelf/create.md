# Create Operation for Book Model

```python
from bookshelf.models import Book

# Create a Book instance using objects.create
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# <Book: 1984 by George Orwell (1949)>
