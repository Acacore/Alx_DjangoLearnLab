from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')



urlpatterns = [
    path("", home, name="home"),
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]