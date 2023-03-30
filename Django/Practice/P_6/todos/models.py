from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=False)
    deadline = models.DateTimeField(auto_now=True)