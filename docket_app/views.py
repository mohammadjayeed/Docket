from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import TaskForm
from .models import TaskBuster


def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Added Task"))
        return redirect("todo")
    else:
        all_tasks = TaskBuster.objects.all()
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        context = {
            'all_tasks':all_tasks
        }
        
        return render(request, 'todolist.html', context)
def todolist_delete(request, pk):
    particular_task = TaskBuster.objects.get(pk=pk)
    particular_task.delete()
    return redirect(request.META['HTTP_REFERER'])


def todolist_edit(request,pk):
    if request.method == 'POST':
        particular_task = TaskBuster.objects.get(pk=pk)
        form = TaskForm(request.POST or None, instance = particular_task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Updated"))
    return redirect(request.META['HTTP_REFERER'])

def todolist_mark_task(request,pk):
    
    particular_task = TaskBuster.objects.get(pk=pk)

    if particular_task.completed == True:
        particular_task.completed = False
    else:
        particular_task.completed = True
    
    particular_task.save()
    
    return redirect(request.META['HTTP_REFERER'])
