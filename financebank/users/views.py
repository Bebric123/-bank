from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

User = get_user_model() 

def your_view_here(request):
    return render(request, 'users/home.html')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('finance_list') 
            else:
                messages.error(request, "Неверные учетные данные")
        return render(request, "users/login.html", {"form": form})

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
            return redirect("home")
        return render(request, "users/register.html", {"form": form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })