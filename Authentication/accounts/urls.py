from django.urls import path
from .views import signup, profile, signin, user_logout
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout')
]
