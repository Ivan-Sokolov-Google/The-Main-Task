from django.contrib import admin
from .models import Teacher, Schedule, Debt, Exam, Department

admin.site.register(Teacher)
admin.site.register(Schedule)
admin.site.register(Debt)
admin.site.register(Exam)
admin.site.register(Department)