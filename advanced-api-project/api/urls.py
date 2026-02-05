from django.urls import path, include
from rest_framework import generics
from rest_framework.routers import DefaultRouter
from .views import (AuthorViewSet,  BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('authors/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='author-list'),
    path('authors/<int:pk>/', AuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='author-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    # path('books/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    # path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]