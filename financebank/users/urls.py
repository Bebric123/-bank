from django.contrib import admin
from django.urls import path, include
# from .views import FinanceListView
from .views import custom_login_view

urlpatterns = [
    # path('', FinanceListView.as_view(), name='users_list'),
    path('login/', custom_login_view, name='login'),
]