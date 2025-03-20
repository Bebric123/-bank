import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import FinanceRecord1

@login_required
def analytics_view(request):
    user = request.user

    total_income = FinanceRecord1.objects.filter(user=user, transaction_type="income").aggregate(Sum("amount"))["amount__sum"] or 0
    total_expense = FinanceRecord1.objects.filter(user=user, transaction_type="expense").aggregate(Sum("amount"))["amount__sum"] or 0

    category_expenses = FinanceRecord1.objects.filter(user=user, transaction_type="expense") \
        .values("category") \
        .annotate(total=Sum("amount")) \
        .order_by("-total")

    category_labels = [item["category"] for item in category_expenses]
    category_values = [float(item["total"]) for item in category_expenses]

    recommendations = []
    if total_expense > total_income * 0.7:
        recommendations.append("Ваши расходы составляют более 70% дохода. Рассмотрите возможность сокращения трат.")
    if any(exp["total"] > total_income * 0.3 for exp in category_expenses):
        recommendations.append("Некоторые категории тратят более 30% вашего дохода. Проверьте, можно ли их уменьшить.")

    context = {
        "total_income": total_income,
        "total_expense": total_expense,
        "category_labels": json.dumps(category_labels),
        "category_values": json.dumps(category_values),
        "recommendations": recommendations
    }

    return render(request, "analytics/analitycs.html", context)