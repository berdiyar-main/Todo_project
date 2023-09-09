from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoModel
from .forms import TodoModelForm
# Create your views here.

class TodoPage(ListView):
    model = TodoModel
    template_name = 'home.html'
    context_object_name = 'object_list'

class TodoDetail(DetailView):
    model = TodoModel
    template_name = 'todo_detail.html'
    context_object_name = 'post'

class TodoCreate(CreateView):
    model = TodoModel
    template_name = 'todo_add.html'
    form_class = TodoModelForm

class TodoEdit(UpdateView):
    model = TodoModel
    form_class = TodoModelForm
    template_name = 'todo_edit.html'

class TodoDelte(DeleteView):
    model = TodoModel
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')