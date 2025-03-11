from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .forms import TaskForm  # We'll create this form next

def task_list(request):
    """View for displaying all tasks with drag-and-drop functionality."""
    tasks = Task.objects.all().order_by('priority')
    form = TaskForm()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

def task_create(request):
    """View for creating a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Set the priority to be after the last task
            last_task = Task.objects.order_by('-priority').first()
            new_priority = 1 if not last_task else last_task.priority + 1
            
            task = form.save(commit=False)
            task.priority = new_priority
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    """View for updating a task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    """View for deleting a task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def task_toggle_complete(request, pk):
    """View for toggling task completion status."""
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@csrf_exempt
@require_POST
def update_task_order(request):
    """API view to update task priorities when tasks are reordered via drag and drop."""
    task_ids = request.POST.getlist('task_ids[]')
    
    for index, task_id in enumerate(task_ids):
        task = Task.objects.get(pk=task_id)
        task.priority = index
        task.save()
    
    return JsonResponse({'status': 'success'})
