from django.urls import path
from .views import FinanceListView

urlpatterns = [
    path('', FinanceListView.as_view(), name='goals_list'),
]