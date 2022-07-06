from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskBuster
from .forms import TaskForm
from django.contrib import messages

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Added Task"))
        return redirect("todo")
    else:
        all_tasks = TaskBuster.objects.all
        context = {
            'all_tasks':all_tasks
        }
        return render(request, 'todolist.html', context)
def todolist_delete(request, pk):
    particular_task = TaskBuster.objects.get(pk=pk)
    particular_task.delete()
    return redirect("todo")


def todolist_edit(request,pk):
    if request.method == 'POST':
        particular_task = TaskBuster.objects.get(pk=pk)
        form = TaskForm(request.POST or None, instance = particular_task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Updated"))
    return redirect("todo")

def todolist_mark_task(request,pk):

    particular_task = TaskBuster.objects.get(pk=pk)
    
    if particular_task.completed == True:
        particular_task.completed = False
    else:
        particular_task.completed = True
    
    print(type(particular_task))
    particular_task.save()



    return redirect("todo")