from rest_framework.test import APITestCase
from rest_framework import status
from shipments.models import Shipment


class ShipmentTests(APITestCase):

    def setUp(self):
        self.shipment = Shipment.objects.create(name='Test shipment', description='A test shipment', status='created')

    def test_list_shipments(self):
        url = '/api/shipments/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_shipment(self):
        url = '/api/shipments/'
        data = {'name': 'New shipment', 'description': 'A new shipment', 'status': 'created'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shipment.objects.count(), 2)

    def test_retrieve_shipment(self):
        url = f'/api/shipments/{self.shipment.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test shipment')

    def test_update_shipment(self):
        url = f'/api/shipments/{self.shipment.id}/'
        data = {'name': 'Updated shipment', 'description': 'An updated shipment', 'status': 'in transit'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.shipment.refresh_from_db()
        self.assertEqual(self.shipment.name, 'Updated shipment')
        self.assertEqual(self.shipment.status, 'in transit')

    def test_delete_shipment(self):
        url = f'/api/shipments/{self.shipment.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Shipment.objects.count(), 0)
