from .views import list_books
from .views import home, book_detail, LibraryDetailView,register, DashboardView,HomeView
from .views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path("", home, name="relationship_app-home"),
    path("books/", list_books, name="relationship_app-book-list"),
    path("books/<int:pk>/", book_detail, name="relationship_app-book-detail"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="relationship_app-library-detail"),
    
    # Authentication
    path('', HomeView.as_view(), name='home'),
  
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"),  name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
]