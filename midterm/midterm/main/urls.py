from django.urls import path
from midterm.main.views import BookViewSet,JournalViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('product', BookViewSet, base_name='midterm.main')
router.register('service', JournalViewSet, base_name='midter.main')


urlpatterns = router.urls