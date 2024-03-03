from django.test import TestCase
from reload.models import Reload, Statistics
from django.utils import timezone

class ReloadModelTest(TestCase):
    def test_reload_save_method(self):
        reload = Reload(quantity=10, cost=100, supplier_debt=50)
        reload.save()
        self.assertEqual(reload.cost_price, 10)  # cost divided by quantity

    def test_update_statistics_on_reload_save(self):
        reload = Reload(quantity=10, cost=100, supplier_debt=50)
        reload.save()
        stats = Statistics.objects.get(id=1)
        self.assertEqual(stats.inventory, 10)
        self.assertEqual(stats.total_supplier_debt, 50)