import datetime

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User


from annoying.fields import AutoOneToOneField


class X(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField('auth.user', blank=True)

class Y(models.Model):
    pass



