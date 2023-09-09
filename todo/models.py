from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(default=datetime.now())
    update_time = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'Todo'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.pk)])
