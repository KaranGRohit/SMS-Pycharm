from django.contrib import admin
from .models import Teacher, Result, Assignments, Attendance
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Result)
admin.site.register(Assignments)
admin.site.register(Attendance)