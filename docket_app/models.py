from django.db import models
from django.contrib.auth.models import User
class TaskBuster(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    task = models.CharField(max_length=400)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "Task no. - " + str(self.id) + ", Completion status: " + str(self.completed)
    
