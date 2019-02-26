from django import forms

from .models import models

class ResultForm(forms.Form):
    Rid = forms.IntegerField()






    Rid = models.IntegerField()
    grade = models.CharField(max_length=4)
    sub1 = models.CharField(max_length=20)
    sub2 = models.CharField(max_length=20)
    sub3 = models.CharField(max_length=20)
    marks1 = models.IntegerField()
    marks2 = models.IntegerField()
    marks3 = models.IntegerField()

