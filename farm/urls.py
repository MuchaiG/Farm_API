from django.urls import path
from .views import (
    FieldListCreateView, CropListCreateView, PlantingListCreateView,
    FieldRetrieveUpdateDestroyView, CropRetrieveUpdateDestroyView, PlantingRetrieveUpdateDestroyView
)

urlpatterns = [
    path('fields/', FieldListCreateView.as_view(), name='field-list-create'),
    path('fields/<int:pk>/', FieldRetrieveUpdateDestroyView.as_view(), name='field-detail'),

    path('crops/', CropListCreateView.as_view(), name='crop-list-create'),
    path('crops/<int:pk>/', CropRetrieveUpdateDestroyView.as_view(), name='crop-detail'),

    path('plantings/', PlantingListCreateView.as_view(), name='planting-list-create'),
    path('plantings/<int:pk>/', PlantingRetrieveUpdateDestroyView.as_view(), name='planting-detail'),
]
