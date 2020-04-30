from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import LoginForm


def connexion(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)

            # TODO Charger listes de projets
            #TODO return render(request, 'taskmanager/connexion.html', locals())

    return render(request, 'taskmanager/connexion.html', locals())

def deconnexion(request):
    return