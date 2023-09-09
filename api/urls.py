from django.urls import path
from .views import TodosApi, TodoApi

urlpatterns = [
    path('', TodosApi.as_view()),
    path('<int:pk>/s', TodoApi.as_view()),
]