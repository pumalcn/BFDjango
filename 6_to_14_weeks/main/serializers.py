from users.serializers import UserSerializer
from rest_framework import serializers
from . import models


class ProjectShortSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = models.Project
        fields = ('id','name','status','creator')

    def validate_status(self, value):
        if value > 3 or value < 1 :
            raise serializers.ValidationError('Project status must be between 1 and 3')
        return value

    def validate_id(self,value):
        if value < 0 :
            raise serializers.ValidationError('Project status must be greater than 0')
        return value


class ProjectSerializer(ProjectShortSerializer):
    class Meta(ProjectShortSerializer.Meta):
        fields = ProjectShortSerializer.Meta.fields + ('description',)


class BlockSerializer(serializers.ModelSerializer):
    project = ProjectShortSerializer(read_only=True)

    class Meta:
        model = models.Block
        fields = '__all__'

    def validate_type_of(self, value):
        if value > 3 or value < 1:
            raise serializers.ValidationError('Block type must be between 1 and 3')
        return value

    def validate_id(self, value):
        if value < 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value


class TaskShortSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    executor = UserSerializer()

    class Meta:
        model = models.Task
        fields = ('id', 'name', 'creator', 'executor')


class TaskSerializer(TaskShortSerializer):
    block = BlockSerializer(read_only=True)

    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('priority', 'description', 'block')

    def validate_id(self, value):
        if value < 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value


class TaskDocumentSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta:
        model = models.TaskDocument
        fields = '__all__'

    def validate_id(self, value):
        if value <= 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value


class TaskCommentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskComment
        fields = ('id', 'task', 'creator', 'created_at')


class TaskCommentSerializer(TaskCommentShortSerializer):
    creator = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta(TaskCommentShortSerializer.Meta):
        model = models.TaskComment
        fields = '__all__'

    def validate_id(self, value):
        if value <= 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value