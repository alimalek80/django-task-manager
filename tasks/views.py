from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
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
    task.completed = True
    task.save()
    return redirect('task_list')


def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('task_list')
