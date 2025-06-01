from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Clear existing listings
        Listing.objects.all().delete()

        # Get or create a host user
        host, _ = User.objects.get_or_create(username='demo_host')

        # Create sample listings
        for i in range(10):
            Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description="This is a sample description.",
                price_per_night=random.uniform(50, 200),
                location=random.choice(["New York", "Paris", "Cairo", "Tokyo"]),
                host=host
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded sample listings."))
