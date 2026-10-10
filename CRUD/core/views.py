from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
# Create your views here.
#Create
def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        roll = request.POST.get('roll')
        semester = request.POST.get('semester')
        
        Student.objects.create(name=name, roll=roll, semester=semester, dept=dept)
    
    return render(request, 'create_student.html')

# Read
def student_list(request): 
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students':students})

def edit_student(request, id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        student.name = request.POST.get('name')
        student.dept = request.POST.get('dept')
        student.roll = request.POST.get('roll')
        student.semester = request.POST.get('semester')
        
        student.save()
        return redirect('student_list')
    
    return render(request, "edit_student.html", {'student':student})

def delete_student(request, id):
    student= get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')
            
    
        