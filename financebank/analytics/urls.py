from django.urls import path
from .views import analytics_view

urlpatterns = [
    path("analytics/", analytics_view, name="analytics"),
]