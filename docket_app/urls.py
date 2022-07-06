from django.urls import path,include
from .views import todolist,todolist_delete,todolist_edit

urlpatterns = [
    path('',todolist,name="todo"),
    path('delete/<int:pk>/',todolist_delete,name="todo_delete"),
    path('edit/<int:pk>/',todolist_edit,name="todo_edit"),
    
    

]