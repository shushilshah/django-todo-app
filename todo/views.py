from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.


def add_task(request):
    tasks = request.POST['title']
    Task.objects.create(title=tasks)
    return redirect("home")


def mark_as_complete(request, pk):
    completed_tasks = get_object_or_404(Task, pk=pk)
    completed_tasks.is_completed = True
    completed_tasks.save()
    return redirect("home")


def mark_as_undone(request, pk):
    undone_tasks = get_object_or_404(Task, pk=pk)
    undone_tasks.is_completed = False
    undone_tasks.save()
    return redirect("home")


def mark_as_delete(request, pk):
    task_to_delete = get_object_or_404(Task, pk=pk)
    task_to_delete.delete()
    return redirect("home")
