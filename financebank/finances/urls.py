from django.urls import path
from .views import finance_dashboard, finance_history

urlpatterns = [
    path('', finance_dashboard, name='finance_list'),
    path('history/', finance_history, name='finance_history'),
]