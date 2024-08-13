
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from book_admin import views as book_admin_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('books/', include('book_admin.urls')),  # Include the book_admin app URLs
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),  # Override the logout view from Django default
    path('accounts/', include('django.contrib.auth.urls')),  # Include the rest of the auth URLs
    path('signup/', book_admin_views.signup, name='signup'),  # Sign-up page
    path('', book_admin_views.home, name='home'),  # Homepage URL
]

