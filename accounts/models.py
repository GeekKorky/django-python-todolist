from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    added_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "Accounts"

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Accounts.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)