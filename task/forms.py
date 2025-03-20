from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):
    """
    TaskForm es un formulario basado en modelos que se utiliza para crear o actualizar
    instancias del modelo Task. Este formulario incluye los siguientes campos:

    - title: Campo para el título de la tarea.
    - description: Campo para la descripción de la tarea.
    - important: Campo booleano para marcar si la tarea es importante.

    La clase Meta define el modelo asociado y los campos que se incluirán en el formulario.
    Los fields vienen del models
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }
