from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search bar for these fields
    search_fields = ('title', 'author')
    
    # Add filter by publication year
    list_filter = ('publication_year',)