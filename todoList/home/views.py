from django.shortcuts import get_object_or_404, render, redirect
from home.models import Task
from home.forms import TaskForm

def home(request):

    context = {'success': False}
    if request.method == 'POST':
        task = request.POST['task']
        desc = request.POST['desc']

        task = Task(task = task , desc = desc)
        task.save()
        context = {'success': True}
        print('The data has been written to the DB')
    return render(request , 'index.html' , context)


def tasks(request):

    allTasks = Task.objects.all()

    context = {'tasks' : allTasks}

    return render(request , 'tasks.html' ,context)

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tasks')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form})