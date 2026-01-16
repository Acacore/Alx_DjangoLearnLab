from .models import *


books = Book.objects.filter(author__name="J.K. Rowling")
libraries = Library.objects.filter(books__title="1984")
librarian = Libarian.objects.get(library__name="Central Library")