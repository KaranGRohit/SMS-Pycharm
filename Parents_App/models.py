
from django.db import models
from django.utils import timezone
import uuid
from Student_App.models import Student

class Parents(models.Model):
    PrSId = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True)
    PrFname = models.CharField(max_length=20)
    PrLname = models.CharField(max_length=20)
    PrContactNo = models.IntegerField()
