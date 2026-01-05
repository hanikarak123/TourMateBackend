"""
URL configuration for TourMateBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
# include function API urls ke liye zaroori hai
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API ke liye route: http://127.0.0.1:8000/api/
    # Yeh request ko tour_spots/urls.py mein bhejega
    path('api/', include('tour_spots.urls')), 
]