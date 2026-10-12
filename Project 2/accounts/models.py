from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class UserType(models.TextChoices):
        RECRUITERS = 'recruiter','Recruiter'
        JOBSEEKERS ='jobseeker','Jobseeker'
    
    display_name = models.CharField(255)
    email = models.EmailField(max_length=254, unique=True)
    user_type = models.CharField(max_length=20, choices=UserType.choices)
    
    def __str__(self):
        return self.display_name
    
    
class Job(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=255)
    number_of_vacancy = models.PositiveIntegerField(default=1)
    category = models.CharField(max_length=120)
    description = models.TextField()
    skills =  models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class RecruiterProfile(models.Model):
    recruiter = models.OneToOneField(User, on_delete=models.CASCADE, related_name="recruiter_profile")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    location = models.TextField()
    total_employee = models.PositiveIntegerField()
    
    

def resume_path(instance, filename):
    return f"resume/user_{instance.jobseekers.id}/{filename}"

class JobseekerProfile(models.Model):
    jobseeker = models.OneToOneField(User, on_delete=models.CASCADE, related_name="jobseeker_profile")
    resume = models.FileField( upload_to=resume_path, blank=True)
    skills = models.TextField(blank=True)
    