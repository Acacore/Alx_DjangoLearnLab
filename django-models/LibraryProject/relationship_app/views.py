from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView

from .models import Library, Book, Author, Librarian
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


class LoginView(LoginView):
    template_name = "login.html"


class LogoutView(LogoutView):
    template_name = "logout.html"    

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'relationship_app/home.html'






class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'relationship_app/dashboard.html'



def home(request):
    return render(request, "relationship_app/home.html")

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "relationship_app/detail_book.html", {"book": book})




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
