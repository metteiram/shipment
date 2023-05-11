from django.db import models

class Shipment(models.Model):
    shipment_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    shipment_date = models.DateField()
    shipment_status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('In transit', 'In transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ))
