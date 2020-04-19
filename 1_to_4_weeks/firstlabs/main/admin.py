from django.contrib import admin
from firstlabs.main import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status', 'creator',)


@admin.register(models.Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_of', 'project')


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'priority', 'creator', 'executor', 'block', 'order')


@admin.register(models.TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'task', 'creator', 'created_at')


@admin.register(models.TaskDocument)
class TaskDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'creator',)