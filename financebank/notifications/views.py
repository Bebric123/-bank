from django.shortcuts import render
from django.views.generic import ListView
from .models import Notification

class FinanceListView(ListView):
    model = Notification
    template_name = 'notifications/notifications_list.html'