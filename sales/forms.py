from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    debt_change = forms.FloatField(required=False, help_text="Use positive value to increase debt, or negative to decrease.")

    class Meta:
        model = Sale
        fields = ['customer_name', 'quantity', 'amount', 'debt_change']
        widgets = {
            'debt_change': forms.NumberInput(attrs={'step': 0.01}),
        }