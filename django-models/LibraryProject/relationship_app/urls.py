from .views import list_books
from .views import home, book_detail, LibraryDetailView,register, DashboardView,HomeView
from .views import LoginView, LogoutView
from django.urls import path
from .admin_view import admin_dashboard
from .librarian_view import librarian_dashboard
from .member_view import member_dashboard
from . import views
from .views import CustomLoginView
from .views import add_book, edit_book, delete_book


urlpatterns = [
    path("", home, name="relationship_app-home"),
    path("books/", list_books, name="relationship_app-book-list"),
    path("books/<int:pk>/", book_detail, name="relationship_app-book-detail"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="relationship_app-library-detail"),
    
    # Authentication
    path('', HomeView.as_view(), name='home'),
  
    path("register/", views.register, name="register"),
    # path("login/", LoginView.as_view(template_name="login.html"),  name="login"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),

    path("books/add/", add_book, name="add_book"),
    path("books/<int:pk>/edit/", edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", delete_book, name="delete_book"),
]