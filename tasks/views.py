from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Task, TaskCategory
from .forms import TaskForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('task_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def task_list(request):
    """View for displaying all tasks with drag-and-drop functionality."""
    tasks = Task.objects.filter(user=request.user).order_by('priority')
    form = TaskForm(user=request.user)
    categories = TaskCategory.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'form': form,
        'categories': categories
    })

@login_required
def task_create(request):
    """View for creating a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Set the priority to be after the last task
            last_task = Task.objects.filter(user=request.user).order_by('-priority').first()
            new_priority = 1 if not last_task else last_task.priority + 1
            
            task = form.save(commit=False)
            task.user = request.user
            task.priority = new_priority
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    """View for updating a task."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    """View for deleting a task."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_toggle_complete(request, pk):
    """View for toggling task completion status."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    messages.success(request, f'Task marked as {"completed" if task.completed else "incomplete"}!')
    return redirect('task_list')

@login_required
@csrf_exempt
@require_POST
def update_task_order(request):
    """API view to update task priorities when tasks are reordered via drag and drop."""
    task_ids = request.POST.getlist('task_ids[]')
    
    for index, task_id in enumerate(task_ids):
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        task.priority = index
        task.save()
    
    return JsonResponse({'status': 'success'})
