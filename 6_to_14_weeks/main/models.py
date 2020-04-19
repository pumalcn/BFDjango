from django.db import models
from users.models import MainUser
from main.constants import PROJECT_STATUSES, PROJECT_IN_PROCESS, PROJECT_FROZEN, PROJECT_DONE, BLOCK_STATUSES, TASKS_DONE, TASKS_FROZEN, TASKS_IN_PROCESS
from utils.upload import task_document_path
from utils.validators import task_document_size,task_document_extension

import datetime


class ProjectManager(models.Manager):

    def frozen_projects(self):
        return self.filter(status=PROJECT_FROZEN)

    def in_process_projects(self):
        return self.filter(status=PROJECT_IN_PROCESS)

    def done_projects(self):
        return self.filter(status=PROJECT_DONE)

    def filter_by_status(self, status):
        return self.filter(status=status)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.PositiveSmallIntegerField(choices=PROJECT_STATUSES, default=PROJECT_IN_PROCESS)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='projects')

    objects = ProjectManager()

    def is_owner(self,request):
        return self.creator.id == request.user.id

    def __str__(self):
        return self.name


class BlockManager(models.Manager):
    def filter_by_name(self, name):
        return self.filter(name=name)


class Block(models.Model):
    name = models.CharField(max_length=255)
    type_of = models.PositiveSmallIntegerField(choices=BLOCK_STATUSES, default=TASKS_IN_PROCESS)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='blocks')

    objects = BlockManager()

    def __str__(self):
        return self.name


class TaskManager(models.Model):
    def filter_by_name(self, name):
        return self.filter(name=name)

    def filter_by_block(self, block):
        return self.filter(block=block)

    def filter_by_priority(self, priority):
        return self.filter(priority=priority)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    priority = models.IntegerField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_tasks')
    executor = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='tasks', null=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='tasks')
    order = models.IntegerField()

    objects = TaskManager()

    def is_owner(self, request):
        return self.creator.id == request.user.id

    def __str__(self):
        return self.name


class TaskDocument(models.Model):
    document = models.FileField(upload_to=task_document_path, validators=[task_document_size, task_document_extension],
                                null=True, blank=True)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='docs')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='docs')

    def is_owner(self, request):
        return self.creator.id == request.user.id


class TaskCommentManager(models.Model):
    def filter_by_task(self, task):
        return self.filter(task=task)

    def filter_by_creator(self, creator):
        return self.filter(creator=creator)


class AbstractComment(models.Model):
    body = models.CharField(max_length=10000)

    class Meta:
        abstract = True


class TaskComment(AbstractComment):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=datetime.datetime.now)

    objects = TaskCommentManager()

    def is_owner(self, request):
        return self.creator.id == request.user.id

    def __str__(self):
        return self.body