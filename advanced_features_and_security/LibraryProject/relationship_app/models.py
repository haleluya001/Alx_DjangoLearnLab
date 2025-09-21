from django.db import models
from django.conf import settings  # For AUTH_USER_MODEL

# ----------------------------
# Author Model
# ----------------------------
'''class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ----------------------------
# Book Model
# ----------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_year = models.IntegerField(default=2000)


    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.publication_year})"


# ----------------------------
# Library Model
# ----------------------------
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


# ----------------------------
# Librarian Model
# ----------------------------
class Librarian(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="relationship_librarian",
        null=True, blank=True
    )
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.user.username
'''

# ----------------------------
# Optional: UserProfile (if you still want roles separated)
# ----------------------------
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
