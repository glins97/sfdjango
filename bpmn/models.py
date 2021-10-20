from django.db import models
from django.contrib.auth.models import User, Group


class FlowElement(models.Model):
    container = models.ForeignKey('FlowElementsContainer', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class FlowNode(FlowElement):
    pass


class SequenceFlow(FlowElement):
    source = models.ForeignKey(FlowNode, related_name='outgoing', on_delete=models.CASCADE)
    target = models.ForeignKey(FlowNode, related_name='incoming', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Activity(FlowNode):
    pass


class FlowElementsContainer(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Process(FlowElementsContainer):
    pass


class Task(Activity):
    pass


class SubProcess(Activity):
    pass


class EventType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Event(FlowNode):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LaneSet(models.Model):
    name = models.CharField(max_length=255)
    container = models.ForeignKey(FlowElementsContainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lane(models.Model):
    name = models.CharField(max_length=255)
    set = models.ForeignKey(LaneSet, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class Bag(models.Model):
    name = models.CharField(max_length=255)
    container = models.ForeignKey(FlowElementsContainer, on_delete=models.CASCADE)
    activities = models.ManyToManyField(Activity)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True) 
