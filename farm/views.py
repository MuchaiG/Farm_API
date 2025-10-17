from rest_framework import generics, permissions
from .models import Field, Crop, Planting
from .serializers import FieldSerializer, CropSerializer, PlantingSerializer

class FieldListCreateView(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [permissions.IsAuthenticated]

class FieldRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [permissions.IsAuthenticated]

class CropListCreateView(generics.ListCreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticated]

class CropRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlantingListCreateView(generics.ListCreateAPIView):
    queryset = Planting.objects.all()
    serializer_class = PlantingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlantingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planting.objects.all()
    serializer_class = PlantingSerializer
    permission_classes = [permissions.IsAuthenticated]

