from .views import BookListView, BookDetailView, create_book, update_book, delete_book
from django.urls import path

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', create_book, name='create_book'),
    path('books/<int:pk>/update/', update_book, name='update_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]