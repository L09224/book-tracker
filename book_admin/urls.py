from django.urls import path
from . import views  # Import views from the current directory
from .views import user_book_list, add_book_to_list

urlpatterns = [
    path('add/', views.add_book, name='add_book'),  # URL for adding a new book
    path('', views.book_list, name='book_list'),  # URL for listing all books
    path('my-books/', views.user_book_list, name='user_book_list'),  # URL for listing user's books
    path('add-book-to-list/', add_book_to_list, name='add_book_to_list'),  # New URL for adding a book
    path('update-progress/<int:pk>/', views.update_progress, name='update_progress'),  # URL for updating progress
]
