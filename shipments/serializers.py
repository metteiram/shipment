from rest_framework import serializers
from .models import Shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('shipment_id', 'customer_name', 'shipment_date', 'shipment_status')
