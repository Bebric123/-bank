from django.shortcuts import render
from django.views.generic import ListView
from .models import FinancialGoal

class FinanceListView(ListView):
    model = FinancialGoal
    template_name = 'goals/goals_list.html'