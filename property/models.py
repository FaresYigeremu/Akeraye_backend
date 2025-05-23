import uuid

from django.conf import settings
from django.db import models

from useraccount.models import User


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    guests = models.IntegerField()
    country = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    category = models.CharField(max_length=255)
    favorited = models.ManyToManyField(User, related_name='favorites', blank=True)
    image = models.ImageField(upload_to='uploads/properties')
     # Added new image fields
    image2 = models.ImageField(upload_to='uploads/properties', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/properties', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads/properties', blank=True, null=True)
    image5 = models.ImageField(upload_to='uploads/properties', blank=True, null=True)

    landlord = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        # Check if the image exists before generating the URL
        if self.image:
            return f'{settings.WEBSITE_URL}{self.image.url}'
        return '' # Or None, depending on desired API output

    # Added methods for the new image URLs
    def image2_url(self):
        if self.image2:
            return f'{settings.WEBSITE_URL}{self.image2.url}'
        return ''

    def image3_url(self):
        if self.image3:
            return f'{settings.WEBSITE_URL}{self.image3.url}'
        return ''

    def image4_url(self):
        if self.image4:
            return f'{settings.WEBSITE_URL}{self.image4.url}'
        return ''

    def image5_url(self):
        if self.image5:
            return f'{settings.WEBSITE_URL}{self.image5.url}'
        return ''


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, related_name='reservations', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_nights = models.IntegerField()
    guests = models.IntegerField()
    total_price = models.FloatField()
    created_by = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)