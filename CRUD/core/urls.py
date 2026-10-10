from django.urls import path
from .views import add_student, student_list, edit_student, delete_student
urlpatterns = [
    path('create/', add_student, name='add_student'),
    path('list/', student_list, name='student_list'),
    path('edit/<int:id>/', edit_student, name="edit_student"),
    path('delete/<int:id>/', delete_student, name="delete_student")
]
