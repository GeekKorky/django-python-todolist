from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Accounts(models.Model):
    username = models.OneToOneField(User)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    description = models.CharField(max_length=100, default='')
    added_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.username