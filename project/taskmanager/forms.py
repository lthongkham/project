from django import forms
from .models import Task, Journal

# Formulaire pour la connexion
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

# Formulaire pour la création de nouvelle tache,
# creee à partir du modele Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

# Formulaire pour la création de nouvelle note dans une tache,
# creee à partir du modele Journal
class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = '__all__'