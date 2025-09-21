from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import CustomUser, Book, Author

# -----------------------------
# Custom User Admin
# -----------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

# Unregister first if already registered to avoid errors
try:
    admin.site.unregister(CustomUser)
except admin.sites.NotRegistered:
    pass

admin.site.register(CustomUser, CustomUserAdmin)

# -----------------------------
# Book Admin
# -----------------------------
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author__name')
    list_filter = ('publication_year',)
    ordering = ('title',)

admin.site.register(Book, BookAdmin)

# -----------------------------
# Author Admin
# -----------------------------
admin.site.register(Author)
