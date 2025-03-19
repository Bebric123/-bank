import csv
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from finances.models import FinanceRecord 

def import_csv(request):
    if request.method == "POST" and request.FILES.get("file"):
        csv_file = request.FILES["file"]
        
        if not csv_file.name.endswith('.csv'):
            return render(request, "integrations/import_csv.html", {"error": "Файл должен быть в формате CSV!"})

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader) 

        for row in reader:
            FinanceRecord.objects.create(
                type=row[0], 
                category=row[1],  
                amount=float(row[2]), 
                date=row[3]  
            )

        return redirect("finance_list") 

    return render(request, "integrations/import_csv.html")