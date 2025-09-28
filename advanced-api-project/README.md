# Advanced API Project

This project demonstrates advanced API development with Django REST Framework (DRF).

## Features
- Custom models: Author, Book
- Nested serializers with validation
- Generic views for CRUD operations
- Permissions:
  - Public read access
  - Authenticated write access

## Endpoints
- `GET /api/books/` → List all books
- `GET /api/books/<id>/` → Retrieve book by ID
- `POST /api/books/create/` → Create a book (auth required)
- `PUT /api/books/<id>/update/` → Update book (auth required)
- `DELETE /api/books/<id>/delete/` → Delete book (auth required)

## Testing
Use Postman or curl to test endpoints.
