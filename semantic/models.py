from django.db import models
from owlready2 import *
from rdflib import plugin 
from rdflib.serializer import Serializer
from django.conf import settings 

import rdflib
import json 
import time
import logging

logger = logging.getLogger(__name__)

class KipoOntology:
    __instance = None
    __kipo = None
    __world = None
    
    @staticmethod
    def getInstance():
        if KipoOntology.__instance == None:
            KipoOntology()

        return KipoOntology.__instance
    
    def __init__(self) -> None:
        if KipoOntology.__instance == None:
            KipoOntology.__instance = self
            loaded = False
            tries = 0
            while not loaded and tries < 4:
                try:
                    self.__world = World()
                    onto_path.append(settings.SEMANTIC["OWL_FILES"]["IMPORT_FOLDER"])
                    #self.setBackEndDatabase(self.__world)
                    self.__world.set_backend(filename = './semantic.sqlite3', exclusive = False)
                    print(settings.SEMANTIC["OWL_FILES"]["OWL_PATH_FILE"])
                    self.__kipo = self.__world.get_ontology(settings.SEMANTIC["OWL_FILES"]["OWL_PATH_FILE"]).load()
                    self.__world.save()
                    loaded = True
                except Exception as e:
                    tries += 1
                    logger.error('Connot load owl file! [Retrying in ' + str(tries*5) + ' sec]')
                    logger.error(e)
                    time.sleep(tries*5)
                    pass
        else:
            raise Exception("Singleton class")
    
    def setBackEndDatabase(self, world) -> None:
        if settings.SEMANTIC['DATABASE']['TYPE'] == 'relational' :
            world.set_backend(filename = settings.DATABASES[settings.SEMANTIC['DATABASE']['SOURCE_NAME']]['NAME'], 
                              exclusive = False)

    @staticmethod
    def getOntology():
        kipoInstance = KipoOntology.getInstance()
        return kipoInstance.__kipo
    
    @staticmethod
    def getWorld():
        kipoInstance = KipoOntology.getInstance()
        return kipoInstance.__world
    
    @staticmethod
    def json_for_graph(g):
        return g.serialize(format='json-ld', indent=4)

class MetaOwl:
    __owlclass = None
    __objClass = None

    def __init__(self, objClazz, owlClazz):
        self.__owlclass = owlClazz
        self.__objClass = objClazz

    def listObj(self) -> list:
        lista = []
        for k in self.listOwl():
            lista.append(self.owlToObj(k))
        return lista
    
    def listOwl(self) -> list:
        kipo = KipoOntology.getOntology()
        lista = kipo.search(type = self.__owlclass)
        return lista

    def owlToObj(self, owlObj):
        pg = self.__objClass()
        pg.name = owlObj.name
        return pg
    
    def objToOwl(self, obj):
        o = self.__owlclass(obj.name)
        return o

class SemanticModel(models.Model):

    storid = models.IntegerField(unique=True, blank=True, null=True)
    
    def listObj(self) -> list:
        lista = []
        for k in self.listOwl():
            lista.append(self.owlToObj(k))
        return lista
    
    def listOwl(self) -> list:
        kipo = KipoOntology.getOntology()
        lista = kipo.search(type = self.semanticClass)
        return lista

    def owlToObj(self, owlObj):
        pg = self.__class__()
        pg.name = owlObj.name
        return pg
    
    def objToOwl(self, obj):
        o = self.semanticClass(obj.name)
        return o

    def isExistsIndividuals(self) -> bool :
        if self.getIndividualsByName():
            return True
        else:        
            return False
    
    def getIndividualsByName(self) :
        kipo = KipoOntology.getOntology()
        for o in kipo.search(type = self.semanticClass):
            if o.name == self.name:
                return o
        return None

    
    class Meta:
        abstract = True
