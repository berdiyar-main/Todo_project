from django import forms
from .models import TodoModel

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'body', 'created', 'update_time']