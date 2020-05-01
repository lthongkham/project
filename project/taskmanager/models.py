from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    Name = models.CharField(max_length=120)
    members = models.ManyToManyField(User, related_name="members")

    def __str__(self):
        return self.Name

class Status(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.IntegerField(default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Journal(models.Model):
    date = models.DateField()
    entry = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)