from django.shortcuts import render
from django.views.generic import ListView
from .models import CustomUser

class FinanceListView(ListView):
    model = CustomUser
    template_name = 'users/users_list.html'