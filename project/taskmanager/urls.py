from django.urls import path
from . import views

urlpatterns = [
    # url pour se connecter au site
    path('connexion', views.connexion, name='connexion'),
    # url pour se déconnecter du site, redirige vers connexion
    path('deconnexion', views.deconnexion),
    # url pour visualiser la liste des projets de l'utilisateur
    path('projects', views.projects),
    # url pour visualiser la liste des tache du projet dont l'id est id_project
    path('project/<int:id_project>', views.project),
    # url pour visualiser le detail de la tache dont l'id est id_task
    path('task/<int:id_task>', views.task),
    # url pour
    path('newtask', views.newtask, name='newtask'),
    path('edittask/<int:id_task>', views.edittask, name='edittask'),
    path('newjournal/', views.newjournal, name='newjournal'),
]