from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    total_pages = models.IntegerField()

    def __str__(self):
        return self.title

class UserBook(models.Model):
    STATUS_CHOICES = [
        ('reading', 'Reading'),
        ('completed', 'Completed'),
        ('to_read', 'Plan to Read'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reading')
    current_page = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"