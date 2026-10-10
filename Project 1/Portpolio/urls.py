from django.urls import path
from .views import *
urlpatterns = [
    path("", portfolio, name="portfolio"),
    path('register/', registration, name="register"),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path("dashboard/", profile, name="dashboard"),
    # Profile
    path("dashboard/profile/", profile, name="profile"),
    # Skill
    path("dashboard/skills/", show_skills, name="skills"),
    path("dashboard/skills/add/", add_skill, name="add_skill"),
    path("dashboard/skills/<int:id>/edit/", edit_skill, name="edit_skill"),
    path("dashboard/skills/<int:id>/delete/", delete_skill, name="delete_skill"),
    # Education
    path("dashboard/education/", show_education, name="education"),
    path("dashboard/education/add/", add_education, name="add_education"),
    path("dashboard/education/<int:id>/edit/", edit_education, name="edit_education"),
    path("dashboard/education/<int:id>/delete/", delete_education, name="delete_education"),
    # Experience
    path("dashboard/experience/", show_experience, name="experience"),
    path("dashboard/experience/add/", add_experience, name="add_experience"),
    path("dashboard/experience/<int:id>/edit/", edit_experience, name="edit_experience"),
    path("dashboard/experience/<int:id>/delete/", delete_experience, name="delete_experience"),

    # Projects
    path("dashboard/projects/", show_projects, name="projects"),
    path("dashboard/projects/add/", add_project, name="add_project"),
    path("dashboard/projects/<int:id>/edit/", edit_project, name="edit_project"),
    path("dashboard/projects/<int:id>/delete/", delete_project, name="delete_project"),
]
