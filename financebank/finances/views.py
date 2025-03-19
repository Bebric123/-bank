from django.shortcuts import render
from django.views.generic import ListView
from .models import FinanceRecord

class FinanceListView(ListView):
    model = FinanceRecord
    template_name = 'finances/finance_list.html'