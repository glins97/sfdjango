from rest_framework.decorators import api_view
from rest_framework.response import Response

from kipco.models import *
from kipco.serializers import *


@api_view(['GET', 'POST'])
def processgoal_list(request):
    if request.method == 'GET':
        items = ProcessGoal.objects.order_by('pk')
        serializer = ProcessGoalSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProcessGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def processgoal_detail(request, pk):
    try:
        item = ProcessGoal.objects.get(pk=pk)
    except ProcessGoal.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProcessGoalSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProcessGoalSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def activity_list(request):
    if request.method == 'GET':
        items = Activity.objects.order_by('pk')
        serializer = ActivitySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def activity_detail(request, pk):
    try:
        item = Activity.objects.get(pk=pk)
    except Activity.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ActivitySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActivitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def activitygoal_list(request):
    if request.method == 'GET':
        items = ActivityGoal.objects.order_by('pk')
        serializer = ActivityGoalSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActivityGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def activitygoal_detail(request, pk):
    try:
        item = ActivityGoal.objects.get(pk=pk)
    except ActivityGoal.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ActivityGoalSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActivityGoalSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def intention_list(request):
    if request.method == 'GET':
        items = Intention.objects.order_by('pk')
        serializer = IntentionSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IntentionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def intention_detail(request, pk):
    try:
        item = Intention.objects.get(pk=pk)
    except Intention.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = IntentionSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IntentionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def desire_list(request):
    if request.method == 'GET':
        items = Desire.objects.order_by('pk')
        serializer = DesireSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DesireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def desire_detail(request, pk):
    try:
        item = Desire.objects.get(pk=pk)
    except Desire.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DesireSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DesireSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def agenttype_list(request):
    if request.method == 'GET':
        items = AgentType.objects.order_by('pk')
        serializer = AgentTypeSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AgentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def agenttype_detail(request, pk):
    try:
        item = AgentType.objects.get(pk=pk)
    except AgentType.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AgentTypeSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AgentTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def agentspecialty_list(request):
    if request.method == 'GET':
        items = AgentSpecialty.objects.order_by('pk')
        serializer = AgentSpecialtySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AgentSpecialtySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def agentspecialty_detail(request, pk):
    try:
        item = AgentSpecialty.objects.get(pk=pk)
    except AgentSpecialty.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AgentSpecialtySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AgentSpecialtySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def agent_list(request):
    if request.method == 'GET':
        items = Agent.objects.order_by('pk')
        serializer = AgentSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def agent_detail(request, pk):
    try:
        item = Agent.objects.get(pk=pk)
    except Agent.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AgentSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AgentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
