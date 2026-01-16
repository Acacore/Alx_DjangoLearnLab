import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample queries demonstrating relationships
def query_books_by_author(author_name):
    """
    Query all books by a specific author
    """
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a specific library
def list_books_in_library(library_name):
    """
    List all books in a library
    """
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Get the librarian for a specific library
def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library
    """
    library = Library.objects.get(name=library_name)
    return library.librarian


# Example usage
if __name__ == "__main__":
    print(query_books_by_author("Chinua Achebe"))
    print(list_books_in_library("Central Library"))
    print(get_librarian_for_library("Central Library"))
