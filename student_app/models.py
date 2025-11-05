from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)  # ФИО
    department = models.CharField(max_length=100)  # Кафедра
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Schedule(models.Model):
    subject = models.CharField(max_length=100)  # Предмет
    room = models.CharField(max_length=50)  # Аудитория
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)  # День недели

class Debt(models.Model):
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    deadline = models.DateField()  # Срок пересдачи
    student = models.CharField(max_length=100)  # Для простоты, имя студента

class Exam(models.Model):
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    questions = models.TextField()  # Вопросы

class Department(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    room = models.CharField(max_length=50)
    work_time = models.CharField(max_length=100)
    employee = models.CharField(max_length=100)  # ФИО работника