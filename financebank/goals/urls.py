from django.urls import path
from .views import financial_goals, create_goal

urlpatterns = [
    path('goals/', financial_goals, name='financial_goals'),
    path('goals/create/', create_goal, name='create_goal'),
]