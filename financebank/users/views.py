from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def custom_login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Перенаправление на главную страницу
            else:
                messages.error(request, "Неверные учетные данные")
    else:
        form = LoginForm()
    
    return render(request, "users/login.html", {"form": form})