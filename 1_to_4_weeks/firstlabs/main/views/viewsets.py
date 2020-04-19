from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from firstlabs.main import models,serializers
from firstlabs.main.permissions import IsOwner,ProjectPermission, BlockPermission, TaskPermission, TaskInsidePermission


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = (ProjectPermission, )


    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)

    @action(methods=['GET',],detail=False)
    def my(self,request):
        projects = models.Project.objects.filter(creator=self.request.user)
        serializers=self.get_serializer(projects,many=True)

        return Response(serializers.data)

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
            res = serializers.TaskSerializer(models.Task.objects.filter(block_id=block.id), many=True)

            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            request.data['block'] = instance.id
            serializer = serializers.TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)


class TaskDetailViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (TaskPermission,)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=(TaskInsidePermission))
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
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=(TaskInsidePermission))
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
            return Response(serializer.errors)


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
