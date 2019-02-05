from django.contrib import admin
from .models import Accountant, Salary, Fees

admin.site.register(Accountant)
admin.site.register(Salary)
admin.site.register(Fees)
