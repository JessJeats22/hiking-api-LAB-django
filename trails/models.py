from django.db import models

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    distance_km = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} ({self.location})'