from django.urls import path
from apps.users.views import register,login

urlpatterns = [
    path('register/' , register , name='register'),
    path('login/' , login , name='login'),
]