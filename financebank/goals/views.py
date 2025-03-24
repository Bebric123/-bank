from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FinancialGoal
from .forms import FinancialGoalForm, UpdateGoalAmountForm

@login_required
def financial_goals(request):
    goals = FinancialGoal.objects.filter(user=request.user)

    if request.method == "POST":
        form = UpdateGoalAmountForm(request.POST)
        if form.is_valid():
            goal_id = request.POST.get("goal_id")
            goal = FinancialGoal.objects.get(id=goal_id, user=request.user)
            amount = form.cleaned_data["amount"]
            goal.current_amount += amount 
            goal.save()
            messages.success(request, f"Вы добавили {amount} к цели '{goal.title}'.")
            return redirect("financial_goals")

    form = UpdateGoalAmountForm()
    return render(request, "goals/financial_goals.html", {"goals": goals, "form": form})

@login_required
def create_goal(request):
    if request.method == "POST":
        form = FinancialGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('financial_goals')
    else:
        form = FinancialGoalForm()
    
    return render(request, 'goals/create_goal.html', {'form': form})

