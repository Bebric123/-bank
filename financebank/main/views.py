from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Transaction, FinancialGoal, Notification, Report
from .forms import TransactionForm, FinancialGoalForm

# Главная страница с аналитикой
@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    income = transactions.filter(category__is_income=True).aggregate(total=models.Sum("amount"))["total"] or 0
    expenses = transactions.filter(category__is_income=False).aggregate(total=models.Sum("amount"))["total"] or 0
    goals = FinancialGoal.objects.filter(user=request.user)

    return render(request, "dashboard.html", {
        "income": income,
        "expenses": expenses,
        "transactions": transactions,
        "goals": goals
    })

# Добавление доходов/расходов
@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("dashboard")
    else:
        form = TransactionForm()
    return render(request, "add_transaction.html", {"form": form})

# Добавление финансовых целей
@login_required
def add_goal(request):
    if request.method == "POST":
        form = FinancialGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect("dashboard")
    else:
        form = FinancialGoalForm()
    return render(request, "add_goal.html", {"form": form})

# Уведомления
@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return JsonResponse({"notifications": list(notifications.values())})

# Экспорт отчетов (заглушка)
@login_required
def export_report(request):
    # Здесь будет логика генерации CSV
    return JsonResponse({"message": "Отчет будет сгенерирован"})