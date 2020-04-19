from firstlabs.users.serializers import UserSerializer
from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = models.Project
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = models.Block
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    executor = UserSerializer()
    block = BlockSerializer()

    class Meta:
        model = models.Task
        fields = '__all__'


class TaskDocumentSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta:
        model = models.TaskDocument
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta:
        model = models.TaskComment
        fields = '__all__'