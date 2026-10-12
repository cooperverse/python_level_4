from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["username", "display_name", "email", "user_type"]
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfile
        fields = ["skills", "resume"]
        widgets = {
            'skills': forms.TextInput(attrs={
                'placeholder': 'e.g. Python, Django, SQL, HTML, CSS'
            })
        }
        
class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ["name", "email", "location", "total_employee"]
        
        widgets = {
            'email' : forms.EmailInput(attrs={
                'placeholder': 'e.g. user@gmail.com'
            })
        }
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "number_of_vacancy", "category", "description", "skills"]