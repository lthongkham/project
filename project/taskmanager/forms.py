from django import forms
from .models import Task

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
