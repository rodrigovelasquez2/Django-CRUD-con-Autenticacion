from django.contrib import admin
from .models import Task

"""
Este módulo se encarga de registrar el modelo Task en el sitio de administración de Django.

1. **Importación de módulos necesarios**:
    - Se importa `admin` desde `django.contrib` para interactuar con el sistema de administración de Django.
    - Se importa el modelo `Task` desde el archivo `models.py` del mismo módulo.

2. **Descripción del propósito**:
    - Al registrar el modelo `Task`, este se vuelve accesible y manejable desde la interfaz de administración de Django.
    - Esto permite a los administradores realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las instancias de `Task`.

3. **Definición de la clase `TaskAdmin`**:
    - Se crea una clase personalizada `TaskAdmin` que hereda de `admin.ModelAdmin`.
    - Se especifica el campo `readonly_fields` para que el campo `created` sea de solo lectura en el panel de administración.
    - Se define `list_display` para mostrar los campos `title`, `created`, `dateCompleted`, `important` y `user` en la lista de objetos del modelo.

4. **Registro del modelo**:
    - Se registra el modelo `Task` junto con la clase personalizada `TaskAdmin` en el sitio de administración de Django.
    - Esto asegura que las configuraciones definidas en `TaskAdmin` se apliquen al modelo `Task` en el panel de administración.
"""

class TaskAdmin(admin.ModelAdmin):
     readonly_fields = ('created',)
     list_display = ('title', 'created', 'dateCompleted', 'important', 'user')

# Register your models here.
admin.site.register(Task, TaskAdmin)
