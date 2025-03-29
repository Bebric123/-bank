import csv
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from finances.models import FinanceRecord

@login_required
def reports_view(request):
    user = request.user
    period = request.GET.get("period", "month") 
    today = datetime.date.today()

    if period == "month":
        start_date = today.replace(day=1)
    elif period == "quarter":
        quarter = (today.month - 1) // 3 + 1
        start_date = datetime.date(today.year, 3 * (quarter - 1) + 1, 1)
    elif period == "year":
        start_date = today.replace(month=1, day=1)
    else:
        start_date = today.replace(day=1) 

    print(f"Выбранный период: {period}, Дата начала: {start_date}") 

    transactions = FinanceRecord.objects.filter(user=user, date__gte=start_date)

    total_income = transactions.filter(transaction_type="income").aggregate(Sum("amount"))["amount__sum"] or 0
    total_expense = transactions.filter(transaction_type="expense").aggregate(Sum("amount"))["amount__sum"] or 0
    balance = total_income - total_expense

    context = {
        "transactions": transactions,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "selected_period": period,
    }
    return render(request, "reports/reports.html", context)


@login_required
def export_csv(request):
    user = request.user
    period = request.GET.get("period", "month")
    today = datetime.date.today()

    if period == "month":
        start_date = today.replace(day=1)
    elif period == "quarter":
        quarter = (today.month - 1) // 3 + 1
        start_date = datetime.date(today.year, 3 * (quarter - 1) + 1, 1)
    elif period == "year":
        start_date = today.replace(month=1, day=1)
    else:
        start_date = today.replace(day=1)

    transactions = FinanceRecord.objects.filter(user=user, date__gte=start_date)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="report_{period}.csv"'

    writer = csv.writer(response)
    writer.writerow(["date", "transaction_type", "category", "amount"])

    for transaction in transactions:
        writer.writerow([transaction.date, transaction.transaction_type, transaction.category, transaction.amount])

    return response