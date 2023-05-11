from rest_framework import generics
from .models import Shipment
from .serializers import ShipmentSerializer

class ShipmentList(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

class ShipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
