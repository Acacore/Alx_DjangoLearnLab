from .views import list_books
from .views import home, book_detail, LibraryDetailView, register_view, login_view, logout_view
from django.urls import path


urlpatterns = [
    path("", home, name="relationship_app-home"),
    path("books/", list_books, name="relationship_app-book-list"),
    path("books/<int:pk>/", book_detail, name="relationship_app-book-detail"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="relationship_app-library-detail"),
    
    # Authentication
    path("register/", register_view, name="relationship_app-register"),
    path("login/", login_view, name="relationship_app-login"),
    path("logout/", logout_view, name="relationship_app-logout"),
]