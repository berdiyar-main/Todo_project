from django.shortcuts import render
from .serializers import TodoModelSerializer
from rest_framework import generics
from todo.models import TodoModel
# Create your views here.

class TodosApi(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer

class TodoApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer