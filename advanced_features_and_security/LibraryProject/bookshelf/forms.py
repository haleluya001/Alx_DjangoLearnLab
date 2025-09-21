# bookshelf/forms.py
from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    """Validated search form to prevent abuse of search inputs."""
    q = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search title or author"})
    )

    def clean_q(self):
        q = self.cleaned_data.get("q", "")
        q = q.strip()
        # Prevent control characters and overly long payloads
        if any(ord(c) < 32 for c in q):
            raise forms.ValidationError("Illegal characters in search term.")
        if len(q) > 100:
            raise forms.ValidationError("Search term too long.")
        return q

class BookForm(forms.ModelForm):
    """ModelForm for creating/updating Book - centralizes validation and sanitization."""
    class Meta:
        model = Book
        fields = ["title", "author", "description", "cover_image"]

    def clean_title(self):
        title = (self.cleaned_data.get("title") or "").strip()
        if not title:
            raise forms.ValidationError("Title is required.")
        # Additional sanitization (example): drop suspicious long whitespace
        return title
