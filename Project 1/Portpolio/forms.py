from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Portfolio, Project, Education, Experience, Skills

class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["full_name", "bio",  "professional_title"]

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "field_of_study", "start_date", "end_date"]
        widgets = {
            "start_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),}
        
class SkillForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = [ "name", "level" ]

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["company", "position", "start_date", "end_date"]

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [ "title", "description", "github_url", "live_link",
        ]