from django.contrib import admin
from .models import Book, UserBook  # Import models
# Register your models here.

# Register the Book model with the admin site
admin.site.register(Book)

# register the UserBook model
admin.site.register(UserBook)