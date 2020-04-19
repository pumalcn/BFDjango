import logging

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.http import Http404
from django.shortcuts import get_object_or_404

from main import models, serializers
from main.permissions import IsOwner, ProjectPermission, BlockPermission, TaskPermission, TaskInsidePermission

logger = logging.getLogger(__name__)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = (ProjectPermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProjectShortSerializer
        return serializers.ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created project: {serializer.data.get('name')}")
        return serializer.data

    @action(methods=['GET'], detail=False)
    def my(self, request):
        projects = models.Project.objects.filter(creator_id=self.request.user.id)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

    @action(methods=['GET', 'POST'], detail=True)
    def blocks(self, request, pk):
        if request.method == 'GET':
            prj = get_object_or_404(models.Project, id=pk)
            res = serializers.BlockSerializer(models.Block.objects.filter(project_id=prj.id), many=True)

            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            request.data['project'] = instance.id
            serializer = serializers.BlockSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created block: {serializer.data.get('name')}")
            return Response(serializer.errors)


class BlockDetailViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = models.Block.objects.all()
    serializer_class = serializers.BlockSerializer
    permission_classes = (BlockPermission,)

    @action(methods=['GET', 'POST'], detail=True)
    def tasks(self, request, pk):
        if request.method == 'GET':
            block = get_object_or_404(models.Block, id=pk)
            res = serializers.TaskShortSerializer(models.Task.objects.filter(block_id=block.id), many=True)

            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            request.data['block'] = instance.id
            serializer = serializers.TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
            return Response(serializer.errors)

    @action(methods=['GET'], detail=False)
    def mytasks(self, request, pk):
        block = get_object_or_404(models.Block, id=pk)
        result = serializers.TaskShortSerializer(
            models.Task.objects.filter(block_id=block.id, executor_id=self.request.user.id), many=True)
        return Response(result.data)


class TaskDetailViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (TaskPermission,)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=(TaskInsidePermission,))
    def comments(self, request, pk):
        if request.method == 'GET':
            task = get_object_or_404(models.Task, id=pk)
            res = serializers.TaskCommentSerializer(models.TaskComment.objects.filter(task_id=task.id), many=True)

            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            request.data['task'] = instance.id
            serializer = serializers.TaskCommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created task's comment: {serializer.data.get('name')}")
            return Response(serializer.errors)

    @action(methods=['GET'], detail=True, permission_classes=(TaskInsidePermission,))
    def mycomments(self, request, pk):
        task = get_object_or_404(models.Task, id=pk)
        res = serializers.TaskCommentSerializer(
            models.TaskComment.objects.filter(task_id=task.id, creator_id=self.request.user.id), many=True)

        return Response(res.data)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=(TaskInsidePermission,))
    def docs(self, request, pk):
        if request.method == 'GET':
            task = get_object_or_404(models.Task, id=pk)
            res = serializers.TaskDocumentSerializer(models.TaskDocument.objects.filter(task_id=task.id), many=True)

            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            request.data['task'] = instance.id
            serializer = serializers.TaskDocumentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created task's doc: {serializer.data.get('name')}")
            return Response(serializer.errors)

    @action(methods=['GET'], detail=True, permission_classes=(TaskInsidePermission,))
    def mydocs(self, request, pk):
        task = get_object_or_404(models.Task, id=pk)
        res = serializers.TaskDocumentSerializer(
            models.TaskDocument.objects.filter(task_id=task.id, creator_id=self.request.user.id), many=True)

        return Response(res.data)


class TaskCommentViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = models.TaskComment.objects.all()
    serializer_class = serializers.TaskCommentSerializer
    permission_classes = (TaskInsidePermission,)


class TaskDocumentDetailViewSet(mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    queryset = models.TaskDocument.objects.all()
    serializer_class = serializers.TaskDocumentSerializer
    permission_classes = (TaskInsidePermission,)