import csv
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from finances.models import FinanceRecord 
from django.contrib.auth.decorators import login_required

@login_required
def import_csv(request):
    if request.method == "POST" and request.FILES["csv_file"]:
        csv_file = request.FILES["csv_file"]
        decoded_file = csv_file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(decoded_file)

        missing_columns = {"transaction_type", "category", "amount", "date"} - set(reader.fieldnames)
        if missing_columns:
            return HttpResponse(f"Ошибка: отсутствуют столбцы {', '.join(missing_columns)}", status=400)

        records = []
        for row in reader:
            try:
                record = FinanceRecord(
                    user=request.user,
                    transaction_type=row.get("transaction_type", "").strip().lower(),
                    category=row.get("category", "").strip(),
                    amount=row.get("amount", 0),
                    date=row.get("date", ""),
                )
                records.append(record)
            except KeyError as e:
                return HttpResponse(f"Ошибка: отсутствует поле {str(e)} в CSV", status=400)
        
        FinanceRecord.objects.bulk_create(records)
        return HttpResponse("Импорт завершен!")

    return render(request, "integrations/import_csv.html")