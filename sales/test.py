from sales.models import Sale
from django.test import TestCase
from reload.models import Reload, Statistics

class SaleModelTest(TestCase):
    def setUp(self):
        Statistics.objects.create(id=1, cost_price=15)  # Pre-populate Statistics

    def test_sale_save_method(self):
        sale = Sale(quantity=3, amount=100)
        sale.save()
        stats = Statistics.objects.get(id=1)
        self.assertEqual(stats.inventory, -3)  # Assuming starting inventory is 0
        self.assertEqual(stats.balance, 100)
        self.assertEqual(sale.profit, 55)  # amount - (quantity * cost_price)