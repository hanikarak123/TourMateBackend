# tour_spots/urls.py (Corrected Code)

from django.urls import path
# Humein Detail View ko import karna hai
from .views import TourSpotListView, TourSpotDetailView 

urlpatterns = [
    # 1. List/All Spots (Home Page API)
    # path('tour-spots/', TouristSpotList.as_view(), name='tourist-spot-list'), <--- Aapke code mein purana naam hai
    path('tour-spots/', TourSpotListView.as_view(), name='tourspot-list'),
    
    # 2. Detail Spot (Detail Page API) <--- YEH LINE ZAROORI HAI!
    # Yeh ID (pk) ko capture karta hai
    path('tour-spots/<int:pk>/', TourSpotDetailView.as_view(), name='tourspot-detail'),
]