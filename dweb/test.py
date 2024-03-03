from dweb.models import Order
from django.test import TestCase
from reload.models import Reload, Statistics

class OrderModelTest(TestCase):
    def setUp(self):
        Statistics.objects.create(id=1, cost_price=20)  # Pre-populate Statistics

    def test_order_save_method(self):
        order = Order(quantity=2)
        order.save()
        stats = Statistics.objects.get(id=1)
        self.assertEqual(stats.inventory, -2)  # Assuming starting inventory is 0
        self.assertEqual(stats.profit, -40)  # quantity * cost_price