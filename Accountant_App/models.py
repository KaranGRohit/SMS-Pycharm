
from django.db import models
from django.utils import timezone
import uuid
from Student_App.models import Student
from Teacher_App.models import Teacher

class Accountant(models.Model):
    Aid = models.IntegerField()
    AFname = models.CharField(max_length=20)
    ALname = models.CharField(max_length=20)
    Email = models.EmailField()


class Salary(models.Model):
    ATid = models.ForeignKey(Teacher, models.SET_NULL, blank=True, null=True)
    exp = models.IntegerField()
    amnt = models.IntegerField()
    sal_date = models.DateField()

class Fees(models.Model):
    ASId = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True)
    fee = models.IntegerField()
    last_date = models.DateField()
    due_charge = models.IntegerField()




