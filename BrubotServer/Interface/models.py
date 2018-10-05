from __future__ import unicode_literals
from django.db import models
from enum import Enum

class StatusChoice(Enum):
    NS = "Not Started"
    ST = "Started"
    FI = "Finished"
    ER = "Error"


class Task(models.Model):

    STATUS_CHOICES = (
        ("NS", "Not Started"),
        ("ST", "Started"),
        ("FI", "Finished"),
        ("ER", "Error"),
    )

    TYPE_CHOICES = (
        ("UD", "Undefined"),
        ("TD", "Torrent Download"),
        ("TS", "Torrent Search"),
    )

    taskName = models.CharField(max_length=128)
    status = models.CharField(max_length=5, default="Not Started", choices=STATUS_CHOICES)
    type = models.CharField(max_length=5, default="Undefined", choices=TYPE_CHOICES)


    def __str__(self):
        return "{} ({})".format(self.taskName, str(self.status))

    def printme(self):
        print("\n")
        print("Task #{}".format(self.id))
        for field in self._meta.get_fields():
            print("\t{}: {}".format(str(field.name), eval("self." + str(field.name))))

    def getDict(self):
        taskDict = {}
        for field in self._meta.get_fields():
            taskDict[str(field.name)] = eval("self." + str(field.name))
        return taskDict


class WorkerStatus(models.Model):

    STATUS_CHOICES = (
        ("Cannot connect", "Cannot connect"),
        ("Working", "Working"),
        ("Idle", "Idle"),
    )

    workerName = models.CharField(max_length=128)
    status = models.CharField(max_length=32, default="Cannot connect", choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
