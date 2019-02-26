from django import forms

from .models import models

class ResultForm(forms.Form):
    Rid = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Rid',
        'id':'Rid',
    }))

    grade = forms.CharField(max_length=4, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'grade',
        'id':'grade',
    }))

    sub1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'sub1',
        'id':'sub1',
    }))

    marks1 = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'marks1',
        'id':'marks1,'
    }))

    sub2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'sub2',
        'id':'sub2',
    }))

    marks2 = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'marks2',
        'id':'marks2',
    }))

    sub3 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'sub3',
        'id':'sub3',
    }))

    marks3 = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'marks3',
        'id':'marks3',
    }))






    Roll_no = models.ForeignKey(Student,on_delete=models.CASCADE)
    Rid = models.IntegerField()
    grade = models.CharField(max_length=4)
    sub1 = models.CharField(max_length=20)
    sub2 = models.CharField(max_length=20)
    sub3 = models.CharField(max_length=20)
    marks1 = models.IntegerField()
    marks2 = models.IntegerField()
    marks3 = models.IntegerField()