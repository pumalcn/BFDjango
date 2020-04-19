from django.db import models
from firstlabs.users.models import MainUser
from firstlabs.main.constants import PROJECT_STATUSES, PROJECT_IN_PROCESS, PROJECT_FROZEN, PROJECT_DONE, BLOCK_STATUSES, TASKS_DONE, TASKS_FROZEN, TASKS_IN_PROCESS
import datetime


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.PositiveSmallIntegerField(choises=PROJECT_STATUSES, default=PROJECT_IN_PROCESS)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='projects')

    def is_owner(self, request):
        return self.creator.id == request.user.id

    def __str__(self):
        return self.name


class Block(models.Model):
    name = models.CharField(max_length=255)
    type_of = models.PositiveSmallIntegerField(choises=BLOCK_STATUSES, default=TASKS_IN_PROCESS)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='blocks')

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    priority = models.IntegerField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_tasks')
    executor = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='tasks', null=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='tasks')
    order = models.IntegerField()

    def is_owner(self, request):
        return self.creator.id == request.user.id

    def __str__(self):
        return self.name


class TaskDocument(models.Model):
    document = models.FileField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='docs')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='docs')

    def is_owner(self, request):
        return self.creator.id == request.user.id


class TaskComment(models.Model):
    body = models.CharField(max_length=10000)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def is_owner(self, request):
        return self.creator.id == request.user.id

    def __str__(self):
        return self.body