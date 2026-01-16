from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView

from .models import *


def home(request):
    return render(request, "relationship_app/home.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "relationship_app/book_detail.html", {"book": book})




class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # optional but clear

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context["books"] = library.books.all()  # Add all books in this library
        context["now"] = timezone.now()
        return context
# Create your views here.
