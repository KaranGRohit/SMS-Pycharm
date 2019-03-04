from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

class IndexView(TemplateView):
    template_name = 'home.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('home')
        else:
            form = UserCreationForm()
            return render(request,'signup.html',{'form':form})




