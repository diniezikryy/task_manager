from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    isCompleted = models.BooleanField(default=False)
    subtasks = models.ManyToManyField("Subtask", related_name="subtasks")
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    column = models.ForeignKey("Column", on_delete=models.CASCADE, null=True, related_name="columns")


    def __str__(self):
        return self.title

class Subtask(models.Model):
    title = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    taskId = models.ForeignKey("Task", on_delete=models.CASCADE, null=True, related_name="task")
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Column(models.Model):
    name = models.CharField(max_length=200)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, related_name="tasks")

    def __str__(self):
        return self.name