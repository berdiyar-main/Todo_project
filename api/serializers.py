from rest_framework import serializers
from todo.models import TodoModel

class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id', 'title', 'body', 'created', 'update_time']