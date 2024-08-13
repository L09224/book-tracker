from django.urls import path
from . import views
from .views import delete_book


urlpatterns = [
    # General listing of all books 
    path('books/', views.book_list, name='book_list'),

    # User-specific book list and actions
    path('my-books/', views.user_book_list, name='user_book_list'),  # List user-specific books
    path('my-books/add/', views.add_book_to_list, name='add_book_to_user_list'), # Add book to user's list
    path('my-books/update/<int:id>/', views.update_progress, name='update_progress'),  # Update progress on a user's book
    path('my-books/delete/<int:id>/', views.delete_book, name='delete_user_book'),  # Delete a user's book
    

    #  other general book actions not tied to a specific user
    path('books/add/', views.add_book, name='add_book'),  
]
