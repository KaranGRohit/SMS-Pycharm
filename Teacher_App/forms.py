from django import forms

from .models import models

class ResultForm(forms.Form):
    Rid = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Rid',
    }))

    grade = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'grade',
    }))

    sub1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'sub1',
    }))

    marks1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'marks1',
    }))

    sub2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'sub2',
    }))

    marks2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'marks2',
    }))

    sub3 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'sub3',
    }))

    marks3 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'marks3',
    }))





