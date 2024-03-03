from django.db import models
from reload.models import Statistics  # Ensure this import path is correct based on your project structure

class Loss(models.Model):
    TYPE_CHOICES = (
        ('usage', 'Usage'),
        ('expense', 'Expense'),
    )

    datetime = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    value = models.FloatField()
    loss = models.FloatField(editable=False)  # Set editable=False to prevent it from being edited in forms

    def save(self, *args, **kwargs):
        # Fetch the single instance of Statistics
        stats = Statistics.objects.get(id=1)  # Assuming a single row for simplicity

        if self.type == 'usage':
            # Use cost_price from the statistics table
            self.loss = self.value * stats.cost_price
            # Update inventory and profit in the statistics table
            stats.inventory -= self.value
            stats.profit -= self.loss
        else:  # type is 'expense'
            self.loss = self.value
            # Subtract the value from balance and profit in the statistics table
            stats.balance -= self.value
            stats.profit -= self.value

        # Save the Loss instance
        super(Loss, self).save(*args, **kwargs)
        # Save the updated statistics
        stats.save()

    def __str__(self):
        return f"{self.datetime} - {self.type} - {self.value} - {self.loss}"