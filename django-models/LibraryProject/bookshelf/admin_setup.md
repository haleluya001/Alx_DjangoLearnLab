# Django Admin Setup for Book Model

## 1. Registration
```python
from django.contrib import admin
from .models import Book
admin.site.register(Book)
