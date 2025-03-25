import csv
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from finances.models import FinanceRecord 
from django.contrib.auth.decorators import login_required

@login_required
def import_csv(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")

        if not csv_file:
            messages.error(request, "Ошибка: Выберите CSV-файл перед загрузкой.")
            return redirect("import_csv")

        decoded_file = csv_file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(decoded_file)

        print(f"Заголовки в CSV: {reader.fieldnames}")

        missing_columns = {"transaction_type", "category", "amount", "date"} - set(reader.fieldnames)
        if missing_columns:
            messages.error(request, f"Ошибка: отсутствуют столбцы {', '.join(missing_columns)}")
            return redirect("import_csv")

        records = []
        for row in reader:
            try:
                record = FinanceRecord(
                    user=request.user,
                    transaction_type=row.get("transaction_type", "").strip().lower(),
                    category=row.get("category", "").strip(),
                    amount=float(row.get("amount", 0)),
                    date = datetime.fromisoformat(row["date"].strip()), 
                )
                records.append(record)
            except KeyError as e:
                messages.error(request, f"Ошибка: отсутствует поле {str(e)} в CSV")
                return redirect("import_csv")
        
        FinanceRecord.objects.bulk_create(records)
        messages.success(request, "Импорт завершен!")
        return redirect("import_csv")

    return render(request, "integrations/import_csv.html")