from django import forms
from .models import FinanceRecord

class TransactionForm(forms.ModelForm):
    class Meta:
        model = FinanceRecord
        fields = ['transaction_type', 'amount', 'category']