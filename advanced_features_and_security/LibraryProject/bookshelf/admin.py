from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')


    
    # Add search bar for these fields
    search_fields = ('title', 'author')
    
    # Add filter by publication year
    list_filter = ('publication_year',)




@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
    )
