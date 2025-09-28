from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers:
    - CRUD operations
    - Filtering, searching, ordering
    - Permissions and authentication
    """

    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')

        # Create authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')

        # Create books
        self.book1 = Book.objects.create(title='Book One', publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2021, author=self.author2)

        # API endpoints
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])

    # -------------------
    # LIST & RETRIEVE TESTS
    # -------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book One')

    # -------------------
    # CREATE TESTS
    # -------------------
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'Book Three',
            'publication_year': 2022,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Book Three',
            'publication_year': 2022,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------------------
    # UPDATE TESTS (PATCH)
    # -------------------
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'Updated Book One'}  # only updating title
        response = self.client.patch(self.update_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    # -------------------
    # DELETE TESTS
    # -------------------
    def test_delete_book_admin(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_non_admin(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------------------
    # FILTERING, SEARCHING, ORDERING TESTS
    # -------------------
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=Book One')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books_by_author(self):
        response = self.client.get(self.list_url + '?search=Author Two')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author2.id)

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.list_url + '?ordering=-publication_year')
        self.assertEqual(response.data[0]['publication_year'], 2021)
