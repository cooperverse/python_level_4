from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["username", "display_name", "email", "user_type"]
        
class LogginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)
    
