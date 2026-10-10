from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    dept = models.CharField(max_length=50)
    roll = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name 