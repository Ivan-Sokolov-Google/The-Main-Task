from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('debts/', views.debts_view, name='debts'),
    path('teachers/', views.teachers_view, name='teachers'),
    path('exams/', views.exams_view, name='exams'),
    path('departments/', views.departments_view, name='departments'),
]