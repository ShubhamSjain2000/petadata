import datetime

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters import rest_framework as filters


from workflow.models import WorkSpace, WorkFlow, WorkFlowTrigger
from workflow.seralizers import (CreateListWorkSpaceSerializer,
                                 RetrieveWorkSpaceSerializer,
                                 CreateListWorkFlowSerializer,
                                 RetrieveWorkFlowSerializer,
                                 CreateListWorkFlowTriggerSerializer,
                                 RetrieveWorkFlowTriggerSerializer)
from workflow.filters import WorkFlowTriggerFilter


class WorkSpaceViewSet(viewsets.ModelViewSet):

    queryset = WorkSpace.objects.all()
    create_list_serializer_class = CreateListWorkSpaceSerializer
    retrieve_serializer_class = RetrieveWorkSpaceSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    name_search = openapi.Parameter('name', openapi.IN_QUERY,
                                    description="name keyword",
                                    type=openapi.TYPE_STRING)
    filter_backends = [filters.DjangoFilterBackend,]
    filter_by = openapi.Parameter('name', openapi.IN_QUERY,
                                 description="field you want to order by to",
                                 type=openapi.TYPE_STRING)
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(participants=self.request.user)

    def perform_create(self, serializer):

        workspace = serializer.save(created_by=self.request.user)
        workspace.participants.set([self.request.user])

    def get_serializer_class(self):

        assert (self.create_list_serializer_class is not None
                and self.retrieve_serializer_class is not None)

        if self.action == 'retrieve':
            return self.retrieve_serializer_class
        return self.create_list_serializer_class

    @swagger_auto_schema(manual_parameters=[filter_by])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path="search")
    @swagger_auto_schema(manual_parameters=[name_search])
    def search_workspace_with_name(self, request, *args, **kwargs):
        name_keyword = request.query_params.get('name')
        qs = WorkSpace.objects.filter(name__startswith=name_keyword,
                                      participants=self.request.user)
        serializer = CreateListWorkSpaceSerializer(qs, many=True)
        return Response(serializer.data)


class WorkFlowViewSet(viewsets.ModelViewSet):

    queryset = WorkFlow.objects.all()
    create_list_serializer_class = CreateListWorkFlowSerializer
    retrieve_serializer_class = RetrieveWorkFlowSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    name_search = openapi.Parameter('name', openapi.IN_QUERY,
                                    description="name keyword",
                                    type=openapi.TYPE_STRING)
    workspace_id = openapi.Parameter('workspace_id', required=True,
                                    type=openapi.TYPE_STRING, in_='path',
                                     )

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_id')
        return self.queryset.filter(workspace_id=workspace_id)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except Exception as e:
            return Response(e,
                            status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        workspace_id=self.kwargs.get('workspace_id')
        workspace = WorkSpace.objects.get(workspace_id=workspace_id)
        serializer.save(created_by=self.request.user, workspace_id=workspace)

    def get_serializer_class(self):

        assert (self.create_list_serializer_class is not None
                and self.retrieve_serializer_class is not None)

        if self.action == 'retrieve':
            return self.retrieve_serializer_class
        return self.create_list_serializer_class

    @action(detail=False, methods=['get'], url_path="search")
    @swagger_auto_schema(manual_parameters=[name_search])
    def search_worksflow_with_name(self, request, *args, **kwargs):
        name_keyword = request.query_params.get('name')
        workspace_id = self.kwargs.get('workspace_id')
        qs = WorkFlow.objects.filter(name__startswith=name_keyword,
                                     workspace_id=workspace_id)
        serializer = CreateListWorkFlowSerializer(qs, many=True)
        return Response(serializer.data)


class WorkFlowTriggerViewSet(viewsets.ModelViewSet):

    queryset = WorkFlowTrigger.objects.all()
    create_list_serializer_class = CreateListWorkFlowTriggerSerializer
    retrieve_serializer_class = RetrieveWorkFlowTriggerSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lower_date_range = openapi.Parameter('lower_date_range', openapi.IN_QUERY,
                                     type=openapi.TYPE_STRING)
    higher_date_range = openapi.Parameter('higher_date_range', openapi.IN_QUERY,
                                     type=openapi.TYPE_STRING)
    workflow_trigger_id = openapi.Parameter('workflow_trigger_id', openapi.IN_QUERY,
                                     type=openapi.TYPE_STRING)
    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_class = WorkFlowTriggerFilter


    def get_queryset(self):
        workflow_id = self.kwargs.get('workflow_id')
        return self.queryset.filter(workflow_id=workflow_id)

    def create(self, request, *args, **kwargs):
        data = {'started_at': datetime.datetime.now()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except Exception as e:
            return Response(e,
                            status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(manual_parameters=[ workflow_trigger_id, lower_date_range, higher_date_range])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        workflow_id=self.kwargs.get('workflow_id')
        workflow = WorkFlow.objects.get(workflow_id=workflow_id)
        serializer.save(triggered_by=self.request.user, workflow_id=workflow)

    def get_serializer_class(self):

        assert (self.create_list_serializer_class is not None
                and self.retrieve_serializer_class is not None)

        if self.action == 'retrieve':
            return self.retrieve_serializer_class
        return self.create_list_serializer_class

    @action(detail=False, methods=['get'], url_path="search")
    # @swagger_auto_schema(manual_parameters=[started_at_gte, started_at_lte])
    def filter_workflow_trigger_with_time(self, request, *args, **kwargs):
        '%Y-%m-%d %H:%M:%S'
        lower_range = datetime.datetime.strptime(request.query_params.get('lower_date_range'),
                                        '%Y-%m-%d %H:%M:%S')
        higher_range = datetime.datetime.strptime(request.query_params.get('higher_date_range'),
                                         '%Y-%m-%d %H:%M:%S')
        workflow_id = self.kwargs.get('workflow_id')
        qs = WorkFlowTrigger.objects.filter(started_at__range=(lower_range,
                                            higher_range),
                                            workflow_id=workflow_id)
        serializer = CreateListWorkFlowTriggerSerializer(qs, many=True)
        return Response(serializer.data)

