from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Project


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
    return render(request, 'taskmanager/projects_list.html', locals())