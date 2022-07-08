from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import TaskForm
from .models import TaskBuster


def index(request):
   
    return render(request, 'index.html',{})
@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request,("Added Task"))
        return redirect("todo")
    else:
        all_tasks = TaskBuster.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        context = {
            'all_tasks':all_tasks
        }
        
        return render(request, 'todolist.html', context)
@login_required
def todolist_delete(request, pk):
    
    try:
        particular_task = TaskBuster.objects.get(pk=pk)
    except:
        return render(request, 'warning.html',{})


    if particular_task.owner == request.user:
        particular_task.delete()
    else:
        messages.error(request,("Restricted"))
    try:
        destination = redirect(request.META['HTTP_REFERER'])
    except KeyError:
        destination = redirect('todo')

    return destination

@login_required
def todolist_edit(request,pk):
    if request.method == 'POST':
        particular_task = TaskBuster.objects.get(pk=pk)

        form = TaskForm(request.POST or None, instance = particular_task)
        
        if form.is_valid():
            form.save()
        messages.success(request,("Task Updated"))


    try:
        destination = redirect(request.META['HTTP_REFERER'])
    except KeyError:
        destination = redirect('todo')

    return destination
@login_required
def todolist_mark_task(request,pk):
    try:
        particular_task = TaskBuster.objects.get(pk=pk)
    except:
        return render(request, 'warning.html',{})

    if particular_task.owner == request.user:

        if particular_task.completed == True:
            particular_task.completed = False
        else:
            particular_task.completed = True
        
        particular_task.save()
    else:

        messages.error(request,("Restricted"))
    
    try:
        destination = redirect(request.META['HTTP_REFERER'])
    except KeyError:
        destination = redirect('todo')

    return destination
