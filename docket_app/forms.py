from .models import TaskBuster
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskBuster
        fields = ['task','completed']