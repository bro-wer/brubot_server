from __future__ import unicode_literals
from django.db import models


class Task(models.Model):
    taskName = models.CharField(max_length=128)
