from django.db import models

# Create your models here.

class Author(models.Model):
    """
      Represents an author who can write one or more books.

    This model stores basic information about an author.
    An Author can be associated with multiple Book instances
    through a one-to-many relationship.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """
    Represents a book written by an author.

    Each Book is linked to a single Author using a ForeignKey.
    The ForeignKey establishes a one-to-many relationship:
    one author can write many books, but each book has only one author.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.DateField()

    def __str__(self):
        return self.title