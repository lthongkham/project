from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, TaskForm, JournalForm
from .models import Project, Task, Journal

'''''
Vue qui permet de se s'identifier comme utilisateur
grace à un formulaire.
Si l'authentification est reussie, la liste des projets apparait.
Sinon, la meme page est envoyee avec un message d'erreur.
'''''
def connexion(request):
    form = LoginForm(request.POST or None)
    # Message d'erreur si l'authentification echoue
    message = None
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            # L'authentification est reussie, on passe à la liste des projets
            return projects(request)
        else:
            message = "Erreur d'authentification"

    return render(request, 'taskmanager/connexion.html', locals())

'''''
Vue qui permet de se deconnecter.
Redirige vers la page de connexion.
'''''
def deconnexion(request):
    logout(request)
    return redirect(connexion)

'''''
Vue qui affiche la liste des projets auquels participe l'utilisateur.
'''''
def projects(request):
    username = request.user.username
    # Recupere les projets ayant pour membre l'utilisateur
    P = Project.objects.filter(members__username = username)
    # Nombre de projets affiché dans la page
    l = len(P)
    return render(request, 'taskmanager/projects.html', locals())

'''''
Vue qui affiche la liste des taches d'un projet.
'''''
def project(request, id_project):
    # Recupere le projet grace à son id
    p = Project.objects.filter(id=id_project)[0]
    # Recupere la liste des taches du projet
    tasks = p.task_set.all()
    return render(request, 'taskmanager/project.html', locals())

'''''
Vue qui affiche les details d'une tache avec son journal.
'''''
def task(request, id_task):
    # Recupere la tache grace à son id
    t = Task.objects.filter(id=id_task)[0]
    # Recupere la liste des entrees du journal d'une tache
    journals = t.journal_set.all()
    return render(request, 'taskmanager/task.html', locals())

'''''
Vue qui permet de creer une nouvelle tache à partir d'un formulaire.
'''''
def newtask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        # Recupere la tache afin d'obtenir son id
        newtask = Task.objects.all()[len(Task.objects.all())-1]
        id_task = newtask.id
        return task(request, id_task)

    return render(request, 'taskmanager/newtask.html', locals())

'''''
Vue qui permet de modifier les attributs d'une tache à partir d'un formulaire pre-rempli.
'''''
def edittask(request, id_task):
    t = Task.objects.filter(id=id_task)[0]
    # Instancie le formulaire à partir de la tache deja existante
    form = TaskForm(request.POST or None, instance = t)
    if form.is_valid():
        form.save()
        return task(request, t.id)

    return render(request, 'taskmanager/edittask.html', locals())

'''''
Vue qui permet de creer une nouvelle entree de journal à partir d'un formulaire.
'''''
def newjournal(request):
    form = JournalForm(request.POST or None)
    if form.is_valid():
        form.save()
        # Recupere l'entree de journal pour obtenir son id
        newjournal = Journal.objects.all()[len(Journal.objects.all())-1]
        id_task = newjournal.task.id
        print(id_task)
        return task(request, id_task)

    return render(request, 'taskmanager/newjournal.html', locals())