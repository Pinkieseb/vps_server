from django.db import models
from reload.models import Statistics  # Ensure this import path is correct based on your project structure
from debtmanager.models import DebtPayment, Customer  # Import DebtPayment and Customer models

class Sale(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    quantity = models.FloatField()
    amount = models.FloatField()
    profit = models.FloatField(editable=False)

    def save(self, *args, debt_change=None, **kwargs):
        # Fetch the single instance of Statistics for the cost_price
        stats = Statistics.objects.get(id=1)  # Assuming a single row for simplicity

        # Calculate profit
        self.profit = self.amount - (self.quantity * stats.cost_price)

        # Update Statistics: subtract quantity from inventory, add amount to balance, and add profit to profit
        stats.inventory -= self.quantity
        stats.balance += self.amount
        stats.profit += self.profit
        stats.save()

        super(Sale, self).save(*args, **kwargs)  # Save the Sale instance before creating DebtPayment

        # If debt_change is provided and not 0, create a DebtPayment
        if debt_change is not None and debt_change != 0:
            customer, _ = Customer.objects.get_or_create(customer_name=self.customer_name)
            if debt_change > 0:
                DebtPayment.objects.create(customer=customer, debt_increase=debt_change, linked_sale=self)
            else:  # debt_change < 0
                DebtPayment.objects.create(customer=customer, debt_decrease=-debt_change, linked_sale=self)

    def __str__(self):
        return f"Sale to {self.customer_name} on {self.datetime}"