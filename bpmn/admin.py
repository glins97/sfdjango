# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *


@admin.register(FlowElement)
class FlowElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'container', 'name', 'description')
    list_filter = ('container',)
    search_fields = ('name',)


@admin.register(FlowNode)
class FlowNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'container', 'name', 'description')
    list_filter = ('container',)
    search_fields = ('name',)


@admin.register(SequenceFlow)
class SequenceFlowAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'container',
        'name',
        'description',
        'source',
        'target',
    )
    list_filter = ('container', 'source', 'target')
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'container',
        'name',
        'description',
        'flowelement_ptr',
    )
    list_filter = ('container', 'flowelement_ptr')
    search_fields = ('name',)


@admin.register(FlowElementsContainer)
class FlowElementsContainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'goal')
    list_filter = ('goal',)
    search_fields = ('name',)


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'goal')
    list_filter = ('goal',)
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
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


@admin.register(SubProcess)
class SubProcessAdmin(admin.ModelAdmin):
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


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'container',
        'name',
        'description',
        'flowelement_ptr',
        'event_type',
    )
    list_filter = ('container', 'flowelement_ptr', 'event_type')
    search_fields = ('name',)


@admin.register(LaneSet)
class LaneSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'container')
    list_filter = ('container',)
    search_fields = ('name',)


@admin.register(Lane)
class LaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'set', 'group')
    list_filter = ('set', 'group')
    search_fields = ('name',)