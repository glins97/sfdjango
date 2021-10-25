from django.db import models
from owlready2 import *
from rdflib import plugin 
from rdflib.serializer import Serializer
from django.conf import settings 

import rdflib
import json 
import time
import logging
import threading

logger = logging.getLogger(__name__)

class KipoOntology:
    _lock = threading.Lock()
 
    @classmethod
    def loadConfig(cls):
        with cls._lock:
            if not hasattr(cls, '_world') or cls._world == None:
                loaded = False
                tries = 0
                while not loaded and tries < 4:
                    try:
                        cls._world = World(filename= settings.SEMANTIC["DATABASE"]["NAME"], exclusive=False)
                        onto_path.append(settings.SEMANTIC["OWL_FILES"]["IMPORT_FOLDER"])
                        cls._kipo = cls._world.get_ontology(settings.SEMANTIC["OWL_FILES"]["OWL_PATH_FILE"]).load()
                        cls._world.save()
                        #sync_reasoner(cls._world)
                        loaded = cls._kipo.loaded
                    except Exception as e:
                        tries += 1
                        logger.error('Connot load owl file! [Retrying in ' + str(tries*5) + ' sec]')
                        logger.error(e)
                        time.sleep(tries*5)

    @classmethod
    def getOntology(cls):
        if not hasattr(cls, '_kipo'):
            cls.loadConfig()
        return cls._kipo
    
    @classmethod
    def getWorld(cls):
        if not hasattr(cls, '_world'):
            cls.loadConfig()
        return cls._world

    @classmethod
    def save(cls):
        world = cls.getWorld()
        world.save()
        sync_reasoner(world)

    
class SemanticModel(models.Model):

    storid = models.IntegerField(unique=False, blank=True, null=True)
    semanticClass = 'Thing'
    
    def listObj(self) -> list:
        lista = []
        for k in self.listOwl():
            lista.append(self.owlToObj(k))
        return lista
    
    def listOwl(self) -> list:
        kipo = KipoOntology.getOntology()
        lista = kipo.search(type = self.getSemanticClass())
        return lista

    def owlToObj(self, owlObj):
        pg = self.__class__()
        pg.name = owlObj.name
        return pg
    
    def objToOwl(self):
        kipo = KipoOntology.getOntology()
        with kipo:
            o = self.getSemanticClass()(self.name)
            self.setIndividualProperties(o)
            KipoOntology.getWorld().save()
            return o

    def isExistsIndividual(self) -> bool :
        if self.getIndividual():
            return True
        else:        
            return False
    
    def getIndividual(self) :
        kipo = KipoOntology.getOntology()
        for o in kipo.search(type = self.getSemanticClass()):
            if o.name == self.name:
                return o
        return None

    def getSemanticClass(self) :
        kipo = KipoOntology.getOntology()
        for i in list(kipo.classes()):
            if i.name == self.semanticClass:
                return i
        return None
    
    def setIndividualProperties(self, owl) :
        pass
    class Meta:
        abstract = True
