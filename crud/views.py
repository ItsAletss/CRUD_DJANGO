from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
import time

# Create your views here.
def task_list_and_create(request):

#logica para crear una tarea y guardarla en mi base de datos ADMIN
    if request.method == 'POST':
        form = TaskForm(request.POST) # crea una instancia del formulario con los datos del POST
        if form.is_valid():
            form.save()
            form = redirect('crud:crud_list')
            print('Tarea creada correctamente')
    else:
        form = TaskForm()
    #tasks = Task.objects.all()

#logica para filtrar las tareas completadas y pendientes
    task_completed = Task.objects.filter(completed=True)
    pending_task = Task.objects.filter(completed=False)

    return render(request, 'task_list.html',{
        'form' : form,
        #'tasks': tasks
        'task_completed' : task_completed,
        'pending_task' : pending_task
    })