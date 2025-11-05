from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('register')

def home(request):
    if not request.user.is_authenticated:
        return redirect('register')  # Перенаправление на регистрацию для неавторизованных
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправление на главную
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def schedule_view(request):
    return render(request, 'schedule.html')

def debts_view(request):
    return render(request, 'debts.html')

def teachers_view(request):
    return render(request, 'teachers.html')

def exams_view(request):
    return render(request, 'exams.html')

def departments_view(request):
    return render(request, 'departments.html')