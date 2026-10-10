from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistration()
    
    return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data= request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    
    return render(request, 'signin.html', {'form':form})        
@login_required
def profile(request):
        
        return render(request, 'profile.html', {'user':request.user})
    
def user_logout(request):
    logout(request)
    return redirect('signin')