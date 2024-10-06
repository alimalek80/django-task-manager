from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm
from django.utils import timezone
from django.http import JsonResponse


# set start_time When Start Task button is pressed
def task_start(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.start_time = timezone.now()
    task.in_progress = True
    task.save()
    return redirect('task_list')


def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    categories = Category.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'form': form,
        'categories': categories,
    })


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('task_list')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


def task_complete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if task.start_time:
        task.end_time = timezone.now()
    task.completed = True
    task.save()
    return redirect('task_list')


def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('task_list')


def task_in_progress(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.in_progress = True
    task.save()
    return redirect('task_list')
