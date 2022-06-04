from django.contrib import admin
from .models import Book, Review

class RewiewInLine(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    inlines = [
        RewiewInLine,
    ]
    list_display = ('title', 'author', 'price')

admin.site.register(Book, BookAdmin) 