from django.db import models

class Author(models.Model):
    """
    Author model represents a writer.
    Each Author can have multiple related books (One-to-Many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a literary work.
    Each Book is linked to a single Author via ForeignKey.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
