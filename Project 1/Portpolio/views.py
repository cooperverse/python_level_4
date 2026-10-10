from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def registration(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()

            Portfolio.objects.create( user=user, full_name=user.username)
            return redirect("login")
        
    else:
        form = UserRegistration(request.POST)
    
    return render(request,"registration.html", {"form":form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
            
            if user is  not None:
                login(request, user)
            return redirect('profile')
            
    else:
        form = LoginForm()
    return render(request, "login.html", {"form":form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    portfolio = request.user.portfolio

    if request.method == "POST":
        form = PortfolioForm(request.POST, instance=portfolio)

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = PortfolioForm(instance=portfolio)

    return render(request, "profile.html", {"form": form})

@login_required
def portfolio(request):
    portfolio = request.user.portfolio

    return render(
        request,
        "portfolio.html",
        {"portfolio": portfolio}
    )

@login_required
def skill_add(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.portfolio = request.user.portfolio
            skill.save()
            
            return redirect('skills')
        
    else:
        form  = SkillForm()
    
    return render(request, "add_skill.html", {"form":form})

def show_skills(request):
    skills = request.user.portfolio.skills.all()
    
    return render(request, "skills.html", {"skills":skills})

def edit_skills(request, id):
    skill = get_object_or_404(Skills, id=id, )
    
    if request.method == "POST":
            form = SkillForm(request.POST, instance=skill)
            if form.is_valid():
                skill.save()
                return redirect('skills')
            
    else:
        form  = SkillForm(instance=skill)
    
    return render(request, "edit_skills.html", {"form":form})
        
        
@login_required
def show_skills(request):

    skills = request.user.portfolio.skills.all()

    return render(request, "show_skill.html", { "skills": skills})


@login_required
def add_skill(request):

    if request.method == "POST":

        form = SkillForm(request.POST)

        if form.is_valid():

            skill = form.save(commit=False)
            skill.portfolio = request.user.portfolio
            skill.save()

            return redirect("skills")

    else:
        form = SkillForm()

    return render(request, "add_skill.html", {
        "form": form
    })


@login_required
def edit_skill(request, id):

    skill = get_object_or_404(
        Skills, id=id)

    if request.method == "POST":

        form = SkillForm(
            request.POST,
            instance=skill
        )

        if form.is_valid():
            form.save()
            return redirect("skills")

    else:
        form = SkillForm(instance=skill)

    return render(request, "edit_skill.html", {
        "form": form
    })


@login_required
def delete_skill(request, id):

    skill = get_object_or_404( Skills, id=id )

    if request.method == "POST":
        skill.delete()

    return redirect("skills")


# EDUCATION

@login_required
def show_education(request):

    educations = request.user.portfolio.educations.all()

    return render(request, "show_education.html", {"educations": educations})


@login_required
def add_education(request):

    if request.method == "POST":

        form = EducationForm(request.POST)

        if form.is_valid():

            education = form.save(commit=False)
            education.portfolio = request.user.portfolio
            education.save()

            return redirect("education")

    else:
        form = EducationForm()

    return render(request, "add_education.html", {"form": form})


@login_required
def edit_education(request, id):

    education = get_object_or_404( Education, id=id)

    if request.method == "POST":

        form = EducationForm(
            request.POST, instance=education
        )

        if form.is_valid():
            form.save()
            return redirect("education")

    else:
        form = EducationForm(instance=education)

    return render(request, "portfolio/edit_education.html", { "form": form })


@login_required
def delete_education(request, id):

    education = get_object_or_404(Education, id=id)

    if request.method == "POST":
        education.delete()

    return redirect("education")



# EXPERIENCE

@login_required
def show_experience(request):

    experiences = request.user.portfolio.experiences.all()
    return render(request, "show_experience.html", {"experiences": experiences})


@login_required
def add_experience(request):

    if request.method == "POST":

        form = ExperienceForm(request.POST)

        if form.is_valid():

            experience = form.save(commit=False)
            experience.portfolio = request.user.portfolio
            experience.save()

            return redirect("experience")

    else:
        form = ExperienceForm()

    return render(request, "portfolio/add_experience.html", { "form": form })


@login_required
def edit_experience(request, id):

    experience = get_object_or_404(Experience, id=id)

    if request.method == "POST":

        form = ExperienceForm( request.POST, instance=experience )

        if form.is_valid():
            form.save()
            return redirect("experience")

    else:
        form = ExperienceForm(instance=experience)

    return render(request, "edit_experience.html", {
        "form": form
    })


@login_required
def delete_experience(request, id):

    experience = get_object_or_404(Experience, id=id)

    if request.method == "POST":
        experience.delete()

    return redirect("experience")


# PROJECTS

@login_required
def show_projects(request):

    projects = request.user.portfolio.projects.all()

    return render(request, "show_project.html", { "projects": projects })


@login_required
def add_project(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)
            project.portfolio = request.user.portfolio
            project.save()

            return redirect("projects")

    else:
        form = ProjectForm()

    return render(request, "add_project.html", { "form": form })


@login_required
def edit_project(request, id):

    project = get_object_or_404( Project, id=id )

    if request.method == "POST":

        form = ProjectForm( request.POST, instance=project )

        if form.is_valid():
            form.save()
            return redirect("projects")

    else:
        form = ProjectForm(instance=project)

    return render(request, "edit_project.html", { "form": form })


@login_required
def delete_project(request, id):

    project = get_object_or_404(
        Project,
        id=id)

    if request.method == "POST":
        project.delete()

    return redirect("projects")

