from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20, default="#3498db")
    
    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=0)  # For ordering tasks
    priority_level = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['priority']  # Default ordering by priority
    
    def __str__(self):
        return self.title
    
    def is_overdue(self):
        if self.due_date and not self.completed:
            return self.due_date < timezone.now().date()
        return False
    
    def is_due_soon(self):
        if self.due_date and not self.completed:
            today = timezone.now().date()
            return (self.due_date - today) <= datetime.timedelta(days=2) and self.due_date >= today
        return False
