from django.urls import path
from . import views

urlpatterns = [
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion),
    path('projects', views.projects),
    path('project/<int:id_project>', views.project),
    path('task/<int:id_task>', views.task),
    path('newtask', views.newtask, name='newtask'),
    path('edittask/<int:id_task>', views.edittask, name='edittask'),
    path('newjournal/', views.newjournal, name='newjournal'),
]