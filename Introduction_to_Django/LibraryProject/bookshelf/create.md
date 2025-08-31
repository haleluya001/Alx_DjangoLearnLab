# Create Operation for Book Model

```python
from bookshelf.models import Book

# Create a Book instance
book1 = Book(title="1984", author="George Orwell", publication_year=1949)
book1.save()

# Expected Output:
# <Book: 1984 by George Orwell (1949)>
