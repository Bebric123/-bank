from django.urls import path
from .views import reports_view, export_csv

urlpatterns = [
    path("reports/", reports_view, name="reports"),
    path("reports/export/", export_csv, name="export_csv"),
]