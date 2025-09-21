# SECURITY.md - LibraryProject

This document summarizes security measures implemented (date: 2025-09-21).

## High-level changes
- DEBUG = False in production (to avoid sensitive info leakage).
- ALLOWED_HOSTS must be set to production hostnames.
- HTTPS enforced (SECURE_SSL_REDIRECT = True). Configure TLS at webserver/load-balancer.
- HSTS configured (SECURE_HSTS_SECONDS = 31536000) — only enable after TLS verification.
- SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE set to True.
- SESSION_COOKIE_HTTPONLY = True to prevent cookies from being read by JS.
- X_FRAME_OPTIONS = DENY, SECURE_CONTENT_TYPE_NOSNIFF = True, SECURE_BROWSER_XSS_FILTER = True.
- Content Security Policy implemented via django-csp (preferred) or manual header.

## Input validation & templates
- All user inputs validated via Django Forms (bookshelf/forms.py).
- ModelForm used for create/update to centralize validation.
- Templates include CSRF tokens and rely on Django autoescaping.
- Avoided `|safe` on user content; use bleach or equivalent sanitizer if HTML needs to be stored/displayed.

## Database safety
- Use Django ORM or parameterized raw SQL (cursor.execute(sql, [params])).
- Avoid building SQL via string interpolation.

## CSP
- Recommended: install `django-csp` and maintain CSP_* settings in settings.py.
- Example manual header included in `search_api` view for ad-hoc usage.

## Testing approach (manual + automated)
- Manual tests: CSRF protected endpoints, cookie flags, HSTS and SSL redirects, CSP header present, attempt XSS strings in fields and confirm they do not execute, attempt SQL-like payloads in search.
- Automated smoke tests provided in `bookshelf/tests.py`.

## Additional notes
- Do not enable HSTS before TLS is correct.
- Remove 'unsafe-inline' from CSP once all inline scripts/styles are moved to external files.
