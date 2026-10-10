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
    recruiters = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs", limit_choices_to={"user_type": "recruiter"})
    title = models.CharField(max_length=255)
    vacancy = models.PositiveIntegerField(default=1)
    category = models.CharField(max_length=120)
    description = models.TextField()
    skills_set =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class RecruitersProfile(models.Model):
    recruiters = models.OneToOneField(User, on_delete=models.CASCADE, related_name="recruiter_profile", limit_choices_to={"user_type": "recruiter"})
    total_employee = models.PositiveIntegerField()
    location = models.TextField()
    

def resume_path(instance, filename):
    return f"resume/user_{instance.jobseekers.id}/{filename}"

class JobseekersProfile(models.Model):
    recruiters = models.OneToOneField(User, on_delete=models.CASCADE, related_name="jobseeker_profile", limit_choices_to={"user_type": "jobseeker"})
    skills_set =  models.TextField()
    resume = models.FileField( upload_to=resume_path, blank=True)