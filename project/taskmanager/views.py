from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, TaskForm
from .models import Project, Task


def connexion(request):
    form = LoginForm(request.POST or None)
    message = None
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)

            # TODO Charger listes de projets
            return projects(request)
        else:
            message = "Erreur d'authentification"

    return render(request, 'taskmanager/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(connexion)

def projects(request):
    username = request.user.username
    P = Project.objects.filter(members__username = username)
    return render(request, 'taskmanager/projects.html', locals())

def project(request, id_project):
    p = Project.objects.all()[id_project-1]
    tasks = p.task_set.all()
    return render(request, 'taskmanager/project.html', locals())

def task(request, id_task):
    task = Task.objects.all()[id_task-1]
    journals = task.journal_set.all()
    return render(request, 'taskmanager/task.html', locals())

def newtask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        id_task = len(Task.objects.all())
        return task(request, id_task)

    return render(request, 'taskmanager/newtask.html', locals())
