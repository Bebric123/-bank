from django.shortcuts import render
from django.views.generic import ListView
from .models import Analytics

class FinanceListView(ListView):
    model = Analytics
    template_name = 'analytics/analytics_list.html'