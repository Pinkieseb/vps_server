from expense.models import Loss
from django.test import TestCase
from reload.models import Reload, Statistics

class LossModelTest(TestCase):
    def setUp(self):
        Statistics.objects.create(id=1, cost_price=10)  # Pre-populate Statistics

    def test_loss_save_method_usage(self):
        loss = Loss(type='usage', value=5)
        loss.save()
        stats = Statistics.objects.get(id=1)
        self.assertEqual(stats.inventory, -5)  # Assuming starting inventory is 0
        self.assertEqual(loss.loss, 50)  # value * cost_price

    def test_loss_save_method_expense(self):
        loss = Loss(type='expense', value=100)
        loss.save()
        stats = Statistics.objects.get(id=1)
        self.assertEqual(stats.balance, -100)
        self.assertEqual(loss.loss, 100)