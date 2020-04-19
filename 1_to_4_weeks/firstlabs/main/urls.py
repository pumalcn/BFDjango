from django.urls import path
from firstlabs.main.views import ProjectViewSet, BlockDetailViewSet, TaskDetailViewSet
from rest_framework import routers

router = routers.DefaultRouter
router.register('projects', ProjectViewSet,basename='main')
router.register('blocks', BlockDetailViewSet,basename='main')
router.register('tasks', TaskDetailViewSet,basename='main')


urlpatterns = router.urls