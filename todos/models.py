from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Friend(models.Model):
    users = models.ManyToManyField(User)