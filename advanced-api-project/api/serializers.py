from .models import Author, Book
from rest_framework import serializers
from datetime import date


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer converts Author model instances into JSON
    and vice versa. It also includes a nested representation
    of books written by the author.
    """
    
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer handles the conversion of Book instances
    to and from JSON format. It includes custom validation to
    ensure the publication year is not set in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Validate that the publication year is not greater than
        the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value