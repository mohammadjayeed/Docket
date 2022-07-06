from django.db import models

class TaskBuster(models.Model):
    task = models.CharField(max_length=400)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "Task no. - " + str(self.id) + ", Completion status: " + str(self.completed)
