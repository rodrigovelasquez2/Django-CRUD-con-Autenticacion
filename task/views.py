from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task

# Create your views here.


def home(request):
    # form se usa en HTML
    return render(request, 'home.html')


def signup(request):
    """
    Maneja la vista para el registro de usuarios.
    Args:
        request (HttpRequest): La solicitud HTTP enviada por el cliente.
    Returns:
        HttpResponse: Renderiza la plantilla 'signup.html' con el formulario de creación de usuario
        o un mensaje de error si las contraseñas no coinciden.
    Comportamiento:
        - Si el método de la solicitud es 'GET', renderiza la plantilla 'signup.html' con el formulario.
        - Si el método de la solicitud es 'POST':
            - Verifica si las contraseñas proporcionadas ('password1' y 'password2') coinciden.
            - Si coinciden, crea un nuevo usuario con el nombre de usuario y contraseña proporcionados.
            - Si no coinciden, no crea el usuario y muestra un mensaje de error.
        - Imprime los datos enviados en la solicitud POST y un mensaje de depuración en la consola.
    """
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:

        if request.POST['password1'] == request.POST['password2']:
            try:
                # Crea el usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                # Guarda el usuario
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Passwords did not match'
        })

# Función para mostrar las tareas


def tasks(request):
    tasks = Task.objects.filter(user=request.user, dateCompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

# Función para cerrar sesión


def signout(request):
    logout(request)
    return redirect('home')


# Función para iniciar sesión
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')


# Create task
def createTask(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect('tasks')
        except ValueError as e:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'An error occurred while creating the task'
            })

# Actualización de una tarea
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user = request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_details.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user = request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError as e:
            return render(request, 'task_details.html', {
                'task': task,
                'form': form,
                'error': 'An error occurred while updating the task'
            })