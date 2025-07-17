from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_image/', blank=True)

    def __str__(self):
        return f"{self.brand} / {self.name} / {self.year}"
