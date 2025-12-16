from django.shortcuts import render
from todo.models import *
from django.http import HttpResponse


def home(request):
    total_tasks = Task.objects.all()
    uncompleted_tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    context = {
        'uncompleted_tasks': uncompleted_tasks,
        'completed_tasks': completed_tasks,
        "total_tasks": total_tasks
    }
    return render(request, 'dashboard.html', context)
