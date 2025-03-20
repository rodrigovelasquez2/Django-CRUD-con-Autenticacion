from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    """
    Modelo que representa una tarea en el sistema.
    Atributos:
        title (CharField): Título de la tarea con un límite máximo de 200 caracteres.
        description (TextField): Descripción opcional de la tarea. Puede estar en blanco.
        created (DateTimeField): Fecha y hora en que se creó la tarea. Se establece automáticamente al crearla.
        dateCompleted (DateTimeField): Fecha y hora en que se completó la tarea. Puede ser nulo.
        important (BooleanField): Indica si la tarea es importante. Por defecto, es False.
        user (ForeignKey): Relación con el modelo User. Cada usuario puede tener múltiples tareas. 
                           Si el usuario es eliminado, sus tareas asociadas también se eliminan.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    
    # Cada user tiene sus propias tareas (user to many task)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """
        Método que devuelve una representación en cadena del objeto Task.
        Retorna:
            str: Cadena que representa la tarea.
            user: Muestra el usuario que tiene esa tarea
        """
        return self.title + '-' + str(self.user.username)
