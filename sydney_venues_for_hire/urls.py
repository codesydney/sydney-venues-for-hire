from django.contrib import admin
from django.urls import path, include  # Make sure to include this

urlpatterns = [
    path('admin/', admin.site.urls),  # This is for the admin site
    path('', include('venues.urls')),  # Include your app's URL patterns
]
