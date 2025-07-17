from django.shortcuts import render, redirect
from .models import Tasks

# Create your views here.
def list_task(request):
    # Trae todas las tareas de la base de datos
    tareas = Tasks.objects.all()
    return render(request, 'list_task.html', {'tareas': tareas})

def guardar_tarea(request):
    # Crea una tarea y la guarda en un la base de datos
    tarea = Tasks(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'], technology=request.POST['tecnologia'])
    tarea.save()
    return redirect('home')

def eliminar_tarea(request, tarea_id):
    # Toma la tarea que conincida con el tarea_id y la elimina
    tarea = Tasks.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home')

def editar_tarea(request, tarea_id):
    # Trae la tarea que coincida con el id que le estamos pasando en tarea_id
    tarea = Tasks.objects.get(id=tarea_id)
    return render(request, 'editar_tarea.html', {'tareas': tarea})

def actualizar_tarea(request, tarea_id):
    # Selecciona la tarea que su id sea igual al que le estemos pasando. luego la actualizará
    tarea = Tasks.objects.get(id=tarea_id)
    tarea.titulo = request.POST['titulo']
    tarea.technology = request.POST['tecnologia']
    tarea.descripcion = request.POST["descripcion"]
    tarea.save()
    return redirect('home')