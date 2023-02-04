from django.contrib import admin
from backend.models import Book, Author


class BookTabularInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookTabularInline]
    list_display = ('pk', 'id', 'name',)
