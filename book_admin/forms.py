from django import forms
from .models import Book, UserBook

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'total_pages']

class UserBookForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ['book', 'status', 'current_page']