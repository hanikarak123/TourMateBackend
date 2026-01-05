# tour_spots/seed_db.py

import os
import django
import sys

# 1. Path Set Karna: Python ko batana ki settings module kahan hai.
# Yeh 'No module named' error ko theek karta hai.
sys.path.append(os.path.abspath('.')) 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TourMateBackend.settings') 

# 2. Django Environment Setup
try:
    django.setup()
except Exception as e:
    # Agar ab bhi error aaye toh user ko pata chalega ki galti yahan hai
    print(f"Error setting up Django environment (Check TourMateBackend path): {e}")
    sys.exit(1)

# Modules ko import karna
from tour_spots.models import TourSpot
from tour_spots.data import UP_TOURIST_SPOTS

def run_seed():
    """Database mein bulk data daalta hai."""
    print("==================================================")
    print("  Database Seeding Shuru Ho Raha Hai (UP Spots)  ")
    print("==================================================")
    
    # Check aur delete logic, taki duplicate data na daalein
    
    # Taj Mahal record ko check karte hain. Agar 10 se kam records hain, toh maan lete hain ki naya data dalna hai.
    if TourSpot.objects.count() < 10: 
        pass # Naya data daalte hain

    added_count = 0
    skipped_count = 0

    for spot_data in UP_TOURIST_SPOTS:
        # Data ko create karte hain agar woh 'name' se pehle se maujood nahi hai
        if not TourSpot.objects.filter(name=spot_data['name']).exists():
            TourSpot.objects.create(**spot_data) 
            print(f"✅ SUCCESS: '{spot_data['name']}' ({spot_data['city']}) daal diya gaya.")
            added_count += 1
        else:
            print(f"⚠️ SKIPPED: '{spot_data['name']}' ({spot_data['city']}) pehle se maujood hai.")
            skipped_count += 1

    print("==================================================")
    print(f"  Result: {added_count} New Spots Added, {skipped_count} Skipped. ")
    print("==================================================")
    print("Database seeding poora hua. Server ko restart karein aur frontend check karein.")

if __name__ == '__main__':
    run_seed()