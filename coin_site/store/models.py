from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('gold', 'Gold Coin'),
        ('silver', 'Silver Coin'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
