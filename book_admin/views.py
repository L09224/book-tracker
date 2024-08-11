from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Book, UserBook
from .forms import BookForm, UserBookForm

# For login
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'book_admin/home.html')

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

@login_required
def user_book_list(request):
    user_books = UserBook.objects.filter(user=request.user)

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        user_book = UserBook.objects.get(id=book_id, user=request.user)
        form = UserBookForm(request.POST, instance=user_book)
        if form.is_valid():
            form.save()
            return redirect('user_book_list')
    else:
        form = UserBookForm()

    return render(request, 'book_admin/user_book_list.html', {'user_books': user_books, 'form': form})


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

# Signup page

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after sign up
            return redirect('book_list')  # Redirect to book list after signing up
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def update_progress(request, pk):
    user_book = UserBook.objects.get(pk=pk, user=request.user)
    if request.method == "POST":
        form = UserBookForm(request.POST, instance=user_book)
        if form.is_valid():
            form.save()
            return redirect('user_book_list')
    else:
        form = UserBookForm(instance=user_book)
    return render(request, 'book_admin/update_progress.html', {'form': form})

@login_required
def my_books(request):
    user_books = UserBook.objects.filter(user=request.user)

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        user_book = UserBook.objects.get(id=book_id, user=request.user)
        form = UserBookForm(request.POST, instance=user_book)
        if form.is_valid():
            form.save()
            return redirect('user_book_list')
    else:
        form = UserBookForm()

    return render(request, 'book_admin/my_books.html', {'user_books': user_books, 'form': form})  # Ensure this is correct

