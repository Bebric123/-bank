from django.contrib import admin
from django.urls import path, include
from .views import LoginView, RegisterView, your_view_here, profile_view

urlpatterns = [
    # path('', your_view_here, name='home'),
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
]