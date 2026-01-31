from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets


from .models import Book



# Create your views here.
def home(request):
    return render(request, "api/home.html")


class BookList(generics.ListAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer