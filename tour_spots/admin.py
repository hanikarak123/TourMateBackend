from django.contrib import admin
from .models import TourSpot 

# Ek custom class banayein jo bataye ki admin panel mein kya dikhana hai
class TourSpotAdmin(admin.ModelAdmin):
    # List view par dikhne wale fields
    list_display = ('name', 'city', 'category', 'status') 
    
    # Edit screen par dikhne wale fields ka order
    # (Maine City ko Name ke turant baad daala hai)
    fields = [
        'name', 
        'city',             # <-- YAHIN PAR CITY FIELD ADD HUA HAI
        'description', 
        'category',
        'latitude',
        'longitude',
        'image_url',        # Maine isse image_url mana hai, agar aapka field alag hai to badal dena
        'status',
    ] 

# Model ko custom class ke saath register karein
admin.site.register(TourSpot, TourSpotAdmin)