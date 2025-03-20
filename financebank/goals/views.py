from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FinancialGoal
from .forms import FinancialGoalForm

@login_required
def financial_goals(request):
    goals = FinancialGoal.objects.filter(user=request.user)
    return render(request, 'goals/financial_goals.html', {'goals': goals})

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