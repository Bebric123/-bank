from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FinanceRecord
from .forms import TransactionForm
from django.db.models import Q

@login_required
def finance_dashboard(request):
    transactions = FinanceRecord.objects.filter(user=request.user).order_by('-date')
    
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('finance_list')
    else:
        form = TransactionForm()

    return render(request, 'finances/finance_list.html', {'transactions': transactions, 'form': form})

def finance_history(request):
    user = request.user
    records = FinanceRecord.objects.filter(user=user)
    
    # Фильтрация
    transaction_type = request.GET.get('transaction_type')
    category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    if transaction_type:
        records = records.filter(transaction_type=transaction_type)
    if category:
        records = records.filter(category=category)
    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])
    
    return render(request, 'finances/history.html', {'records': records})