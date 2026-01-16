from .views import home, list_book, book_detail, LibraryDetailView
from django.urls import path


urlpatterns = [
    path("", home, name="relationship_app-home"),
    path("books/", book_list, name="relationship_app-book-list"),
    path("books/<int:pk>/", book_detail, name="relationship_app-book-detail"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="relationship_app-library-detail"),
]