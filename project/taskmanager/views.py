from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, TaskForm, JournalForm
from .models import Project, Task, Journal
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
    p = Project.objects.filter(id=id_project)[0]
    tasks = p.task_set.all()
    return render(request, 'taskmanager/project.html', locals())

def task(request, id_task):
    t = Task.objects.filter(id=id_task)[0]
    journals = t.journal_set.all()
    return render(request, 'taskmanager/task.html', locals())

def newtask(request):
    form = TaskForm(request.POST or None)
    #form = TaskForm(request.POST or None, initial={'project': Project.objects.filter(id=id_project)[0]})
    if form.is_valid():
        form.save()
        newtask = Task.objects.all()[len(Task.objects.all())-1]
        id_task = newtask.id
        return task(request, id_task)

    return render(request, 'taskmanager/newtask.html', locals())

def edittask(request, id_task):
    t = Task.objects.filter(id=id_task)[0]
    form = TaskForm(request.POST or None, instance = t)
    if form.is_valid():
        form.save()
        return task(request, t.id)

    return render(request, 'taskmanager/edittask.html', locals())

def newjournal(request):
    form = JournalForm(request.POST or None)
    if form.is_valid():
        form.save()
        newjournal = Journal.objects.all()[len(Journal.objects.all())-1]
        id_task = newjournal.task.id
        print(id_task)
        return task(request, id_task)

    return render(request, 'taskmanager/newjournal.html', locals())