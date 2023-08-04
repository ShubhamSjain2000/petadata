from rest_framework import serializers

from workflow.models import WorkSpace, WorkFlow, WorkFlowTrigger
from auth_management.serializers import UserSerializer


class RetrieveWorkFlowTriggerSerializer(serializers.ModelSerializer):

    triggered_by = UserSerializer(read_only=True)
    class Meta:
        model = WorkFlowTrigger
        fields = ['workflow_trigger_id','started_at', 'ended_at', 'status', 'triggered_by']
        read_only_fields = ['workflow_trigger_id', 'triggered_by']


class RelationWorkFlowTriggerSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkFlowTrigger
        fields = ['workflow_trigger_id']
        read_only_fields = ('workflow_trigger_id',)


class CreateListRelationWorkFlowSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkFlow
        fields = ['name', 'workflow_id']
        read_only_fields = ('workflow_id',)

    def is_valid(self, raise_exception=False):

        if not isinstance(self.initial_data.get('name'), str):
            raise (serializers.ValidationError(detail="name should be a string",
                                               code=400))
        return super().is_valid(raise_exception)


class RetrieveWorkFlowSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(read_only=True)
    workflow_triggers = RelationWorkFlowTriggerSerializer(many=True)

    class Meta:
        model = WorkFlow
        fields = ['workflow_id', 'name', 'created_by', 'workflow_triggers']



class CreateListWorkSpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSpace
        fields = ['name', 'workspace_id']
        read_only_fields = ('workspace_id',)

    def is_valid(self, raise_exception=False):

        if not isinstance(self.initial_data.get('name'), str):
            raise (serializers.ValidationError(detail="name should be a string",
                                               code=400))
        return super().is_valid(raise_exception)


class RetrieveWorkSpaceSerializer(serializers.ModelSerializer):

    participants = UserSerializer(read_only=True, many=True)
    created_by = UserSerializer(read_only=True)
    workflows = CreateListRelationWorkFlowSerializer(many=True)

    class Meta:
        model = WorkSpace
        fields = ['name', 'created_by', 'participants', 'workflows']


class CreateListWorkFlowSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkFlow
        fields = ['name', 'workflow_id']
        read_only_fields = ('workflow_id',)

    def is_valid(self, raise_exception=False):

        if not isinstance(self.initial_data.get('name'), str):
            raise (serializers.ValidationError(detail="name should be a string",
                                               code=400))
        return super().is_valid(raise_exception)


class CreateListWorkFlowTriggerSerializer(serializers.ModelSerializer):
    triggered_by = UserSerializer(read_only=True)
    workflow_id = CreateListRelationWorkFlowSerializer
    class Meta:
        model = WorkFlowTrigger
        fields = ['started_at', 'ended_at', 'status', 'triggered_by',
                  'workflow_trigger_id', 'workflow_id']
        read_only_fields = ['started_at', 'ended_at', 'status', 'triggered_by',
                            'workflow_id', 'workflow_trigger_id']




