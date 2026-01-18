from .views import list_books
from .views import home, book_detail, LibraryDetailView,SignUpView, DashboardView,HomeView
from .views import LoginView, LogoutView, RegisterView
from django.urls import path


urlpatterns = [
    path("", home, name="relationship_app-home"),
    path("books/", list_books, name="relationship_app-book-list"),
    path("books/<int:pk>/", book_detail, name="relationship_app-book-detail"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="relationship_app-library-detail"),
    
    # Authentication
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    
]