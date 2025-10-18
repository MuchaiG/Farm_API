from django.db import models
from farm.models import Planting

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('seeds', 'Seeds'),
        ('fertilizer', 'Fertilizer'),
        ('pesticides', 'Pesticides'),
        ('water', 'Water'),
        ('labor', 'Labor'),
        ('other', 'Other'),
    ]
    planting = models.ForeignKey(Planting, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_incurred = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount} for {self.planting.crop.name}"
