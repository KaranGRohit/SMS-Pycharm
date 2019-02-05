
from django.db import models
from django.utils import timezone
import uuid
from Student_App.models import Student
from Teacher_App.models import Teacher

class Accountant(models.Model):
    ATid = models.ForeignKey(Teacher, models.SET_NULL, blank=True, null=True)
    Aid = models.IntegerField()
    AFname = models.CharField(max_length=20)
    ALname = models.CharField(max_length=20)
    Email = models.EmailField()
    salary = models.IntegerField()
    fee = models.IntegerField()
