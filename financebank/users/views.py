from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()  # Используем кастомную модель пользователя

def your_view_here(request):
    return render(request, 'users/users_list.html')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "users/users_list.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users_list')  # Перенаправление на главную страницу
            else:
                messages.error(request, "Неверные учетные данные")
        return render(request, "users/users_list.html", {"form": form})

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                messages.error(request, "Пользователь с таким именем уже существует.")
                return render(request, "users/register.html", {"form": form})

            user = form.save()
            login(request, user)
            return redirect("users_list")
        return render(request, "users/register.html", {"form": form})