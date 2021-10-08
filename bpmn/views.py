from rest_framework.decorators import api_view
from rest_framework.response import Response
from bpmn.models import *
from bpmn.serializers import *


@api_view(['GET', 'POST'])
def flowelement_list(request):
    if request.method == 'GET':
        items = FlowElement.objects.order_by('pk')
        serializer = FlowElementSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlowElementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def flowelement_detail(request, pk):
    try:
        item = FlowElement.objects.get(pk=pk)
    except FlowElement.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = FlowElementSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlowElementSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def flownode_list(request):
    if request.method == 'GET':
        items = FlowNode.objects.order_by('pk')
        serializer = FlowNodeSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlowNodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def flownode_detail(request, pk):
    try:
        item = FlowNode.objects.get(pk=pk)
    except FlowNode.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = FlowNodeSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlowNodeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def sequenceflow_list(request):
    if request.method == 'GET':
        items = SequenceFlow.objects.order_by('pk')
        serializer = SequenceFlowSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SequenceFlowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def sequenceflow_detail(request, pk):
    try:
        item = SequenceFlow.objects.get(pk=pk)
    except SequenceFlow.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = SequenceFlowSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SequenceFlowSerializer(item, data=request.data)
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
def flowelementscontainer_list(request):
    if request.method == 'GET':
        items = FlowElementsContainer.objects.order_by('pk')
        serializer = FlowElementsContainerSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlowElementsContainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def flowelementscontainer_detail(request, pk):
    try:
        item = FlowElementsContainer.objects.get(pk=pk)
    except FlowElementsContainer.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = FlowElementsContainerSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlowElementsContainerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def process_list(request):
    if request.method == 'GET':
        items = Process.objects.order_by('pk')
        serializer = ProcessSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def process_detail(request, pk):
    try:
        item = Process.objects.get(pk=pk)
    except Process.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProcessSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProcessSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        items = Task.objects.order_by('pk')
        serializer = TaskSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        item = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def subprocess_list(request):
    if request.method == 'GET':
        items = SubProcess.objects.order_by('pk')
        serializer = SubProcessSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def subprocess_detail(request, pk):
    try:
        item = SubProcess.objects.get(pk=pk)
    except SubProcess.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = SubProcessSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubProcessSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def eventtype_list(request):
    if request.method == 'GET':
        items = EventType.objects.order_by('pk')
        serializer = EventTypeSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def eventtype_detail(request, pk):
    try:
        item = EventType.objects.get(pk=pk)
    except EventType.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = EventTypeSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def event_list(request):
    if request.method == 'GET':
        items = Event.objects.order_by('pk')
        serializer = EventSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk):
    try:
        item = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = EventSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def laneset_list(request):
    if request.method == 'GET':
        items = LaneSet.objects.order_by('pk')
        serializer = LaneSetSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LaneSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def laneset_detail(request, pk):
    try:
        item = LaneSet.objects.get(pk=pk)
    except LaneSet.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = LaneSetSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaneSetSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def lane_list(request):
    if request.method == 'GET':
        items = Lane.objects.order_by('pk')
        serializer = LaneSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def lane_detail(request, pk):
    try:
        item = Lane.objects.get(pk=pk)
    except Lane.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = LaneSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaneSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
