from rest_framework import generics
from .models import Venue
from .serializers import VenueSerializer

class VenuesPlaceList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
