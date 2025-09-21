from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Author
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from .forms import BookSearchForm, BookForm
from django.http import JsonResponse, HttpResponse

@require_http_methods(["GET"])
def book_list(request):
    """
    Safe book list / search:
    - Uses a validated BookSearchForm (avoids using raw request.GET values directly)
    - Uses Django ORM (parameterized) rather than raw SQL
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            books = Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q)).distinct()
        else:
            books = Book.objects.all()[:100]  # pagination is recommended in a real app
    # The template relies on Django autoescape; do not use |safe on user fields.
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})


@require_http_methods(["GET", "POST"])
def book_create(request):
    """
    Safe create view:
    - Uses a ModelForm to validate and sanitize data
    - No @csrf_exempt: Django's CSRF middleware protects this POST
    """
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect("bookshelf:book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.publication_year = request.POST.get('publication_year')
        author_id = request.POST.get('author')
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'bookshelf/book_form.html', {'book': book, 'authors': authors})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

@require_http_methods(["GET"])
def search_api(request):
    """
    Example API-style response that sets a manual CSP header, if you choose not to use django-csp.
    Returns JSON results of a safe ORM search.
    """
    form = BookSearchForm(request.GET or None)
    results = []
    if form.is_valid() and form.cleaned_data.get("q"):
        q = form.cleaned_data["q"]
        qs = Book.objects.filter(title__icontains=q).values("id", "title")[:20]
        results = list(qs)
    response = JsonResponse({"results": results})
    # If you're not using django-csp middleware, set the header per-response:
    response["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self';"
    return response

# Demonstration of safe raw SQL use (if ever needed)
def example_safe_raw_sql(title_param):
    """
    If you need raw SQL for a special case, always parameterize using the DB API (%s).
    DO NOT use Python string formatting to build SQL.
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title FROM bookshelf_book WHERE title = %s", [title_param])
        return cursor.fetchall()
