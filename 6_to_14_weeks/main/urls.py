from django.urls import path
from main.views import ProjectViewSet, BlockDetailViewSet, TaskDetailViewSet, TaskDocumentDetailViewSet, TaskCommentViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('blocks', BlockDetailViewSet)
router.register('tasks', TaskDetailViewSet)
router.register('docs', TaskDocumentDetailViewSet)
router.register('comments', TaskCommentViewSet)


urlpatterns = router.urls