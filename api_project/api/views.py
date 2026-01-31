from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from .models import Book



# Create your views here.
def home(request):
    return render(request, "api/home.html")


class BookList(ListAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    