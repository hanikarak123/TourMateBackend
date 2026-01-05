# tour_spots/models.py

from django.db import models

class TourSpot(models.Model):
    # Required fields
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='City Not Specified') 
    description = models.TextField()
    category = models.CharField(max_length=50)
    
    # Optional/Detailed fields
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    image_url = models.URLField(max_length=200, default='https://example.com/default.jpg')
    
    # Status choices
    STATUS_CHOICES = [
        ('Pending Approval', 'Pending Approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending Approval',
    )

    def __str__(self):
        return self.name