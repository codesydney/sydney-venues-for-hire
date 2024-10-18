from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('venues.urls')),
]
