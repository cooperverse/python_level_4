from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, RecruiterProfileForm, JobForm, JobSeekerProfileForm
from .models import User, RecruiterProfile, JobseekerProfile, Job

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {"form":form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                if user.user_type == User.UserType.RECRUITERS:
                    return redirect("recruiter_dashboard")
                return redirect("jobseeker_dashboard")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {"form":form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def recruiter_dashboard(request):
    profile = RecruiterProfile.objects.get(recruiter = request.user)
    
    if request.method == "POST":
        form = RecruiterProfileForm(request.POST, instance=profile)
        
        if form.is_valid():
            profile = form.save(commit=False)
            profile.recruiter = request.user
            profile.save()
            
            return redirect("recruiter_dashboard")
    
    else:
        form = RecruiterProfileForm(instance = profile)
    jobs = Job.objects.filter(recruiter=request.user)
    return render(request, "recruiter_dashboard.html", {"form":form, "profile":profile, "jobs":jobs})

def jobseeker_dashboard(request):
    profile = JobseekerProfile.objects.get(jobseeker=request.user)
    
    if request.method == "POST":
            form = JobSeekerProfileForm(request.POST, instance=profile)
            
            if form.is_valid():
                profile = form.save(commit=False)
                profile.jobseeker = request.user
                profile.save()
                
                return redirect("recruiter_dashboard")
        
    else:
        form = JobSeekerProfileForm(instance = profile)
            
    return render(request, "jobseeker_dashboard.html", {"form":form, "profile":profile})

def add_jobs(request):
    if request.method == "POST":
        form  = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            return redirect("recruiter_dashboard")
    
    else:
        form = JobForm()
    
    return render(request, "add_jobs.html", {"form":form})



        
        
