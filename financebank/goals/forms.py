from django import forms
from .models import FinancialGoal

class FinancialGoalForm(forms.ModelForm):
    class Meta:
        model = FinancialGoal
        fields = ['title', 'target_amount', 'current_amount', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class UpdateGoalAmountForm(forms.Form):
    amount = forms.DecimalField(label="Сумма пополнения", max_digits=10, decimal_places=2, min_value=0.01)