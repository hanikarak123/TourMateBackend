# tour_spots/views.py (Corrected Code)

from rest_framework import generics
from .models import TourSpot
from .serializers import TourSpotSerializer

# 1. List View (Home Page ke liye)
class TourSpotListView(generics.ListAPIView):
    queryset = TourSpot.objects.all()
    serializer_class = TourSpotSerializer

# 2. Detail View (Detail Page ke liye)
class TourSpotDetailView(generics.RetrieveAPIView):
    queryset = TourSpot.objects.all()
    serializer_class = TourSpotSerializer