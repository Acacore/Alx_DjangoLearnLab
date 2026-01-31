from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from .models import Book



# Create your views here.
def home(request):
    return render(request, "api/home.html")


class BookList(generics.ListAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
   