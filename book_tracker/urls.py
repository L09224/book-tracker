"""
URL configuration for book_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from book_admin import views as book_admin_views  # Import views from book_admin

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('books/', include('book_admin.urls')),  # Include the book_admin app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's auth URLs
    path('signup/', book_admin_views.signup, name='signup'),  # Sign-up page
]

