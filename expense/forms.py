from django import forms
from .models import Loss

class LossForm(forms.ModelForm):
    class Meta:
        model = Loss
        fields = ['type', 'value']