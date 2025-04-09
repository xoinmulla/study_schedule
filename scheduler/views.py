# scheduler/views.py

from django.shortcuts import render
from .models import Course, StudySession, Task

def home(request):
    return render(request, 'scheduler/index.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'scheduler/courses.html', {'courses': courses})

def session_list(request):
    sessions = StudySession.objects.all()
    return render(request, 'scheduler/sessions.html', {'sessions': sessions})

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'scheduler/tasks.html', {'tasks': tasks})
