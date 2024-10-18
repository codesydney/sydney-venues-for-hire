from django.urls import path
from . import views

urlpatterns = [
    path('', views.VenuesPlaceList.as_view(), name='place-list'),
]