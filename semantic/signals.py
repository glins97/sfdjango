from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from semantic.models import SemanticModel
from kipco.models import * 

@receiver(pre_save)
def pre_save(sender, instance, **kwargs):
    if SemanticModel in instance.__class__.__bases__ :
        ontoInd = instance.getIndividualsByName() 
        if not ontoInd :
            ontoInd = instance.semanticClass(instance.name)
        
        instance.storid = ontoInd.storid
        
@receiver(post_save)
def post_save(sender, instance, **kwargs):
    if SemanticModel in instance.__class__.__bases__ :
        pass
