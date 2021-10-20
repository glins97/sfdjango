# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *


@admin.register(ProcessGoal)
class ProcessGoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(IntensiveProcess)
class IntensiveProcessAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'goal', 'storid')
    list_filter = ('goal',)
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'container',
        'name',
        'description',
        'flowelement_ptr',
        'flownode_ptr',
    )
    list_filter = ('container', 'flowelement_ptr', 'flownode_ptr')
    search_fields = ('name',)


@admin.register(ActivityGoal)
class ActivityGoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'activity')
    list_filter = ('activity',)
    search_fields = ('name',)


@admin.register(Intention)
class IntentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'activity')
    list_filter = ('activity',)
    search_fields = ('name',)


@admin.register(Desire)
class DesireAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'intention')
    list_filter = ('intention',)
    search_fields = ('name',)


@admin.register(AgentType)
class AgentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(AgentSpecialty)
class AgentSpecialtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    list_filter = ('type',)
    raw_id_fields = ('specialties', 'desires')
    search_fields = ('name',)