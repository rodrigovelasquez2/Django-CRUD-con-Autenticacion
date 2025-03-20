from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                # Guarda el usuario
                user.save()
                return HttpResponse('User Created successfully')
            except:
                return HttpResponse('User already exists')
        return HttpResponse('Passwords do not match')
 