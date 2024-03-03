from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Reload(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField()
    cost = models.FloatField()
    supplier_debt = models.FloatField()
    cost_price = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        self.cost_price = self.cost / self.quantity if self.quantity else 0
        super(Reload, self).save(*args, **kwargs)

    class Meta:
        db_table = 'reloads'

class Statistics(models.Model):
    inventory = models.FloatField(default=0.0)
    balance = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)
    last_reload = models.DateTimeField(null=True, blank=True)
    cost_price = models.FloatField(default=0.0)
    total_supplier_debt = models.FloatField(default=0.0)

    class Meta:
        db_table = 'statistics'

@receiver(post_save, sender=Reload)
def update_statistics(sender, instance, **kwargs):
    stats, created = Statistics.objects.get_or_create(id=1)  # Assuming a single row for simplicity
    stats.inventory = instance.quantity
    stats.balance = 0.0
    stats.profit = 0.0
    stats.last_reload = instance.datetime
    stats.cost_price = instance.cost_price
    stats.total_supplier_debt = instance.supplier_debt
    stats.save()