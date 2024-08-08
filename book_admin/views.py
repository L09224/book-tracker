from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Book, UserBook
from .forms import BookForm, UserBookForm

#temporarily edited out
#class HomePage(TemplateView):
#    """
#    Displays home page"
#    """
#    template_name = 'index.html'

# Create your views here.

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_admin/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_admin/book_list.html', {'books': books})

def user_book_list(request):
    user_books = UserBook.objects.filter(user=request.user)
    return render(request, 'book_admin/user_book_list.html', {'user_books': user_books})

def update_progress(request, pk):
    user_book = UserBook.objects.get(pk=pk)
    if request.method == "POST":
        form = UserBookForm(request.POST, instance=user_book)
        if form.is_valid():
            form.save()
            return redirect('user_book_list')
    else:
        form = UserBookForm(instance=user_book)
    return render(request, 'book_admin/update_progress.html', {'form': form})