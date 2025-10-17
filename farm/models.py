from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Field(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    size_in_acres = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Crop(models.Model):
    CROP_TYPES = [
        ('VEG', 'Vegetable'),
        ('FRUIT', 'Fruit'),
        ('HERB', 'Herb'),
    ]
    name = models.CharField(max_length=50, unique=True)
    crop_type = models.CharField(max_length=10, choices=CROP_TYPES)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Planting(models.Model):
    MATURITY_CHOICES = [
        ('seedling', 'Seedling'),
        ('vegetative', 'Vegetative'),
        ('flowering', 'Flowering'),
        ('harvest', 'Ready for Harvest'),
    ]
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    planting_date = models.DateField()
    maturity_stage = models.CharField(max_length=20, choices=MATURITY_CHOICES)
    expected_harvest_date = models.DateField()
    expected_yield = models.FloatField()
    farm_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.crop.name} in {self.field.name} planted on {self.planting_date}"