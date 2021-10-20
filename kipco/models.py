from django.db import models
from bpmn.models import Activity as BpmnActivity, FlowElementsContainer
from semantic.models import *
from owlready2 import *




class ProcessGoal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Owl(MetaOwl):
        def __init__(self, clazz):
            kipo = KipoOntology.getOntology()
            super().__init__(clazz, kipo.KIPCO__Process_Goal)

class IntensiveProcess(SemanticModel, FlowElementsContainer):
    semanticClass = KipoOntology.getOntology().KIPCO__Knowledge_Intensive_Process
    goal = models.ForeignKey(ProcessGoal, on_delete=models.CASCADE, blank=True, null=True)

class Activity(BpmnActivity):
    
    class Owl(MetaOwl):
        def __init__(self, clazz):
            kipo = KipoOntology.getOntology()
            super().__init__(clazz, kipo.KIPCO__Knowledge_Intensive_Activity)


class ActivityGoal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Owl(MetaOwl):
        def __init__(self, clazz):
            kipo = KipoOntology.getOntology()
            super().__init__(clazz, kipo.KIPCO__Activity_Goal)


class Intention(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Owl():
        kipo = KipoOntology.getOntology()
        pass

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
    class Owl():
        pass




