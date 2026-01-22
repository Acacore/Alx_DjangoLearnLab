from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, ExampleForm
from django.db.models import Q

# View to create a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

# View to edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'form': form})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})


def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )
    return render(request, 'bookshelf/book_list.html', {'books': books})



# View for listing all books
def book_list(request):
    # Use only() to fetch only needed fields
    books = Book.objects.only('title', 'author', 'publication_year')
    return render(request, 'bookshelf/book_list.html', {'books': books})


# View for creating a new book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'form': form})



# ALX expects this example form view
def example_form_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        return redirect('example_form')
    return render(request, 'bookshelf/form_example.html', {'form': form})
