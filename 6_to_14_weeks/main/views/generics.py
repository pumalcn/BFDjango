from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import authenticate, TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView

from main import models, serializers
from main.permissions import IsOwner, ProjectPermission, BlockPermission, TaskPermission, TaskInsidePermission


@permission_classes((ProjectPermission,))
@authentication_classes((JSONWebTokenAuthentication, ))
class ProjectList(APIView):
    def get(self, request):
        projects = models.Project.objects.for_user(request.user)
        serializer = serializers.ProjectSerializer(projects, many=True)
        return Response(serializer.data)

@permission_classes((BlockPermission,))
@authentication_classes((JSONWebTokenAuthentication, ))
class BlockList(APIView):
    def get(self, request):
        block = models.Block.objects.for_user(request.user)
        serializer = serializers.BlockSerializer(block, many=True)
        return Response(serializer.data)

@permission_classes((TaskPermission,))
@authentication_classes((JSONWebTokenAuthentication, ))
class TaskList(APIView):
    def get(self, request):
        tasks = models.Task.objects.for_user(request.user)
        serializer = serializers.TaskShortSerializer(tasks, many=True)
        return Response(serializer.data)

@permission_classes((TaskInsidePermission,))
@authentication_classes((JSONWebTokenAuthentication, ))
class TaskCommentList(APIView):
    def get(self, request):
        tasks = models.TaskComment.objects.for_user(request.user)
        serializer = serializers.TaskCommentSerializer(tasks, many=True)
        return Response(serializer.data)