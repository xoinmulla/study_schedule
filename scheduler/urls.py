# scheduler/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='courses'),
    path('sessions/', views.session_list, name='sessions'),
    path('tasks/', views.tasks_list, name='tasks'),
]
