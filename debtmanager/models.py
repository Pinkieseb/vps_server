from django.db import models
from django.utils import timezone
from django.apps import apps  # Import apps

class Customer(models.Model):
    customer_name = models.CharField(max_length=255, unique=True)
    total_debt = models.FloatField(default=0.0)
    last_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name

class DebtPayment(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='debt_payments')
    debt_increase = models.FloatField(default=0.0)
    debt_decrease = models.FloatField(default=0.0)
    # Use get_model to dynamically retrieve the Sale model
    linked_sale = models.ForeignKey('sales.Sale', on_delete=models.SET_NULL, null=True, blank=True, related_name='debt_payments')

    def save(self, *args, **kwargs):
        # Dynamically retrieve the Sale model inside the method to avoid import issues
        Sale = apps.get_model('sales', 'Sale')
        # Debugging: Print before updating
        print(f"Before Update: Customer's Total Debt: {self.customer.total_debt}")
        
        # Update Customer's total_debt and last_change
        self.customer.total_debt += self.debt_increase - self.debt_decrease
        self.customer.last_change = timezone.now()
        
        # Debugging: Print after updating
        print(f"After Update: Customer's Total Debt: {self.customer.total_debt}")
        
        self.customer.save()

        super(DebtPayment, self).save(*args, **kwargs)
        # Debugging: Confirm save method is called
        print("DebtPayment save method called successfully.")

    def __str__(self):
        return f"{self.datetime} - {self.customer.customer_name}"