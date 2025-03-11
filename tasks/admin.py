from django.contrib import admin
from .models import Task, TaskCategory

@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'priority_level', 'category', 'due_date', 'completed', 'created_at')
    list_filter = ('completed', 'priority_level', 'category', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('priority',)
    date_hierarchy = 'created_at'
    list_editable = ('priority_level', 'category', 'completed')
    readonly_fields = ('created_at', 'updated_at')
