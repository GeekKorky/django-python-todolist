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
    current_user = models.ForeignKey(
        User,
        related_name='owner',
        null=True,
        on_delete=models.CASCADE,
    )

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)
