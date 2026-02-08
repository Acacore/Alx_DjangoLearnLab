from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
import django_filters

class AuthorViewSet(viewsets.ModelViewSet):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 

class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    # filterset_class = BookFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]   