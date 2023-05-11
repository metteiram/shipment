from django.urls import path
from .views import ShipmentList, ShipmentDetail

urlpatterns = [
    path('shipments/', ShipmentList.as_view(), name='shipment-list'),
    path('shipments/<str:pk>/', ShipmentDetail.as_view(), name='shipment-detail'),
]
