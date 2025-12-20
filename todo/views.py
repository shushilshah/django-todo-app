from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.http import HttpResponse
from .ai_utils import parse_task
from django.utils.dateparse import parse_datetime
# Create your views here.


def add_task(request):
    if request.method == 'POST':
        user_text = request.POST["title"]

        ai_data = parse_task(user_text)

        Task.objects.create(
            title=ai_data['title'],
            due_date=parse_datetime(
                ai_data['due_date']) if ai_data['due_date'] else None,
            priority=ai_data['priority'],
            category=ai_data['category']
        )
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
