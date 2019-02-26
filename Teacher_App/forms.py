from django import forms

from .models import models

from Student_App.models import Student

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



