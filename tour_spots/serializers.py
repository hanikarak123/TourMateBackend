# tour_spots/serializers.py

from rest_framework import serializers
from .models import TourSpot # Ensure correct model name is imported

class TourSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourSpot
        # All fields to be included in the API response
        fields = [
            'id', 
            'name', 
            'city', 
            'description', 
            'category', 
            'latitude', 
            'longitude', 
            'image_url', 
            'status'
        ]
        # Fields that should not be edited via API
        read_only_fields = ['id', 'status']