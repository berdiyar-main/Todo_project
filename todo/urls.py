from django.urls import path
from .views import TodoPage, TodoCreate, TodoDetail, TodoEdit, TodoDelte

urlpatterns = [
    path('todo_delete/<int:pk>/', TodoDelte.as_view(), name='todo_delete'),
    path('todo/<int:pk>/edit/', TodoEdit.as_view(), name='todo_edit'),
    path('todo/add/', TodoCreate.as_view(), name='todo_add'),
    path('', TodoPage.as_view(), name='home'),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
]