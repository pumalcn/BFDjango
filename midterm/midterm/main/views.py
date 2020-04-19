from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.http import Http404
from django.shortcuts import get_object_or_404

from midterm.main import models, serializers, permissions

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.BookPermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BookShortSerializer
        return serializers.BookSerializer

class JournalViewSet(viewsets.ModelViewSet):
    queryset = models.Journal.objects.all()
    serializer_class = serializers.JournalSerializer
    permission_classes = (permissions.JournalPermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.JournalShortSerializer
        return serializers.JournalSerializer
