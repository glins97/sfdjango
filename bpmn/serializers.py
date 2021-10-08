from rest_framework.serializers import ModelSerializer
from bpmn.models import FlowElement, FlowNode, SequenceFlow, Activity, FlowElementsContainer, Process, Task, SubProcess, EventType, Event, LaneSet, Lane


class FlowElementSerializer(ModelSerializer):

    class Meta:
        model = FlowElement
        fields = '__all__'


class FlowNodeSerializer(ModelSerializer):

    class Meta:
        model = FlowNode
        fields = '__all__'


class SequenceFlowSerializer(ModelSerializer):

    class Meta:
        model = SequenceFlow
        fields = '__all__'


class ActivitySerializer(ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'


class FlowElementsContainerSerializer(ModelSerializer):

    class Meta:
        model = FlowElementsContainer
        fields = '__all__'


class ProcessSerializer(ModelSerializer):

    class Meta:
        model = Process
        fields = '__all__'


class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class SubProcessSerializer(ModelSerializer):

    class Meta:
        model = SubProcess
        fields = '__all__'


class EventTypeSerializer(ModelSerializer):

    class Meta:
        model = EventType
        fields = '__all__'


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class LaneSetSerializer(ModelSerializer):

    class Meta:
        model = LaneSet
        fields = '__all__'


class LaneSerializer(ModelSerializer):

    class Meta:
        model = Lane
        fields = '__all__'
