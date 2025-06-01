from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'listing', 'start_date', 'end_date')

    def __str__(self):
        return f"Booking by {self.user.username} for {self.listing.title}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()  # e.g., 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'listing')

    def __str__(self):
        return f"{self.rating} stars by {self.user.username} for {self.listing.title}"
