from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')




urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('api-token-auth/', views.obtain_auth_token),
]