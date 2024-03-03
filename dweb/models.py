from django.db import models
from reload.models import Statistics  # Ensure this import path is correct based on your project structure

class Order(models.Model):
    POSTAGE_CHOICES = (
        ('Standard', 'Standard'),
        ('Express', 'Express'),
    )

    datetime = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    quantity = models.FloatField()
    postage_type = models.CharField(max_length=8, choices=POSTAGE_CHOICES)
    full_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    suburb = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    tracking_number = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Fetch the single instance of Statistics
        stats = Statistics.objects.get(id=1)  # Assuming a single row for simplicity

        # Calculate the cost of the order
        order_cost = self.quantity * stats.cost_price

        # Update inventory and profit in the statistics table
        stats.inventory -= self.quantity
        stats.profit -= order_cost

        # Save the updated statistics
        stats.save()

        # Save the Order instance
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_id} by {self.username}"