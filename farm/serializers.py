from rest_framework import serializers
from .models import Field, Crop, Planting

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class PlantingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planting
        fields = '__all__'
