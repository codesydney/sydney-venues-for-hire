from django.urls import path
from . import views

urlpatterns = [
    path('venues/', views.get_all_venues, name='get_all_venues'),
    path('venues/<int:objectid>/', views.get_venue_by_id, name='get_venue_by_id'),
]
