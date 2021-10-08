from django.db import models
from bpmn.models import Activity as BpmnActivity

class ProcessGoal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Activity(BpmnActivity):
    pass


class ActivityGoal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Intention(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Desire(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    intention = models.ForeignKey(Intention, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AgentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class AgentSpecialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=100)
    specialties = models.ManyToManyField(AgentSpecialty)
    desires = models.ManyToManyField(Desire)
    type = models.ForeignKey(AgentType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




