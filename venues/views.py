from django.shortcuts import render
from rest_framework import generics
from .models import VenuesForHire
from .serializers import SydneyVenueSerializer

class NSWSchoolList(generics.ListCreateAPIView):
    queryset = VenuesForHire.objects.all()
    serializer_class = SydneyVenueSerializer
