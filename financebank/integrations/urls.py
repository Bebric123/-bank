from django.urls import path
from .views import import_csv

urlpatterns = [
    path("import-csv/", import_csv, name="import_csv"),
]