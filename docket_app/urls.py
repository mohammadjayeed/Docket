from django.urls import path,include
from .views import todolist,todolist_delete,todolist_edit,todolist_mark_task

urlpatterns = [
    path('',todolist,name="todo"),
    path('delete/<int:pk>/',todolist_delete,name="todo_delete"),
    path('edit/<int:pk>/',todolist_edit,name="todo_edit"),
    path('mark/<int:pk>/',todolist_mark_task,name="todo_mark"),
    

    
    

]