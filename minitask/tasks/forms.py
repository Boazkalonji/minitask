

from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titre', 'description', 'statut']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la tâche'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (optionnelle)', 'rows': 4}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }