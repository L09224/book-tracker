from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, UserBook
from .forms import BookForm, UserBookForm

# Views

def custom_logout_view(request):
    
    logout(request)
    
    return render(request, 'registration/logged_out.html')

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
    sort = request.GET.get('sort', 'title')  # Default sorting by title (A-Z)
    direction = request.GET.get('direction', 'asc')  # Default direction is ascending

    if sort == 'title':
        books = Book.objects.all().order_by('title' if direction == 'asc' else '-title')
    elif sort == 'page_count':
        books = Book.objects.all().order_by('total_pages' if direction == 'asc' else '-total_pages')
    else:
        books = Book.objects.all()

    return render(request, 'book_admin/book_list.html', {'books': books, 'sort': sort, 'direction': direction})

@login_required
def user_book_list(request):
    # Get sorting parameters from the request
    sort = request.GET.get('sort', 'book__title')  # Default sorting by book title (A-Z)
    direction = request.GET.get('direction', 'asc')  # Default direction is ascending

    # Apply sorting to the user_books queryset
    if sort == 'book__title':
        user_books = UserBook.objects.filter(user=request.user).order_by('book__title' if direction == 'asc' else '-book__title')
    elif sort == 'book__author':
        user_books = UserBook.objects.filter(user=request.user).order_by('book__author' if direction == 'asc' else '-book__author')
    elif sort == 'book__total_pages':
        user_books = UserBook.objects.filter(user=request.user).order_by('book__total_pages' if direction == 'asc' else '-book__total_pages')
    else:
        user_books = UserBook.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserBookForm(request.POST)
        if form.is_valid():
            user_book = form.save(commit=False)
            user_book.user = request.user
            user_book.save()
            messages.success(request, "Book added/updated successfully.")
            return redirect('user_book_list')
        else:
            messages.error(request, "Failed to add/update the book. Please check your entries.")
    else:
        form = UserBookForm()

    books = Book.objects.all()

    return render(request, 'book_admin/user_book_list.html', {
        'user_books': user_books,
        'books': books, 
        'form': form,
        'sort': sort,
        'direction': direction,
    })


@login_required
def delete_book(request, id):
    # Ensure that only the owner can delete their book
    book = get_object_or_404(UserBook, id=id, user=request.user)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book successfully deleted.")
        return redirect('user_book_list')
    else:
        messages.error(request, "Invalid request.")
        return redirect('user_book_list')

@login_required
def update_progress(request, id):
    user_book = get_object_or_404(UserBook, id=id, user=request.user)
    if request.method == 'POST':
        form = UserBookForm(request.POST, instance=user_book)
        
        # Print form errors for debugging
        if form.is_valid():
            form.save()
            messages.success(request, "Book progress updated successfully.")
            return redirect('user_book_list')
        else:
            # Debug: print form errors to the console
            print("Form errors:", form.errors)
            messages.error(request, "Update failed. Please check your form entries.")
    
    return redirect('user_book_list')


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

    return render(request, 'book_admin/my_books.html', {'user_books': user_books, 'form': form})

@login_required
def add_book_to_list(request):
    books = Book.objects.all()  # Fetch all books
    user_books = UserBook.objects.filter(user=request.user)  # Fetch the user's current book list
    
    if request.method == 'POST':
        form = UserBookForm(request.POST)
        selected_book = request.POST.get('book')
        
        # Check if the book is already in the user's list
        if UserBook.objects.filter(user=request.user, book_id=selected_book).exists():
            messages.error(request, "You have already added this book to your list.")
        elif form.is_valid():
            new_user_book = form.save(commit=False)
            new_user_book.user = request.user
            new_user_book.save()
            messages.success(request, "New book added to your list successfully.")
            return redirect('user_book_list')
        else:
            messages.error(request, "Failed to add book. Please check your entries.")
    
    else:
        form = UserBookForm()

    # Always pass user_books to the template
    return render(request, 'book_admin/user_book_list.html', {
        'form': form,
        'books': books,
        'user_books': user_books
    })
