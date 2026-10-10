from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    
class Portfolio(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolio')
    full_name = models.CharField(max_length=255)
    professional_title = models.CharField(max_length=120, null=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.full_name
    
class Education(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=120)
    field_of_study = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.degree

class Skills(models.Model):
    class Level(models.TextChoices):
        BEGINNER = "beginner", "Beginner"
        INTERMEDIATE = "intermediate", "Intermediate"
        PROFESSIONAL = "professional", "Professional"
        
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=120)
    level=models.CharField(max_length=30, choices=Level.choices)
    
    def __str__(self):
        return self.name
    
    
class Experience(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='experiences')
    
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.position} - {self.company}"
    
class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='projects')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_url = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    
    def __str__(self):
        return self.title