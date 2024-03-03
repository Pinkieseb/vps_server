from django import forms
from .models import Reload

class ReloadForm(forms.ModelForm):
    class Meta:
        model = Reload
        fields = ['quantity', 'cost', 'supplier_debt']