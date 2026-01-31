from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]