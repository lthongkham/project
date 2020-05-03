from django import forms
from .models import Task, Journal

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class TaskForm(forms.ModelForm):
    '''''
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['project'].disabled = True
'''''
    class Meta:
        model = Task
        fields = '__all__'
        readonly_fields = ["project"]

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = '__all__'