from django import forms
from .models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        initial=timezone.now().date
    )
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority_level', 'category', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'priority_level': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } 