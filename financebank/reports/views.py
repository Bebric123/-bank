from django.shortcuts import render
from django.views.generic import ListView
from .models import Report

class FinanceListView(ListView):
    model = Report
    template_name = 'reports/reports_list.html'