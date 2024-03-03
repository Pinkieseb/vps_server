from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('tracking_number',)

class TrackingNumberForm(forms.Form):
    order_id = forms.IntegerField(widget=forms.HiddenInput())
    tracking_number = forms.CharField(label='Tracking Number', max_length=255)