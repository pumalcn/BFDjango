from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from midterm.auth_.models import MainUser,Profile
from midterm.auth_.serializers import UserSerializer


class RegisterUserAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            profile = Profile(user=MainUser.objects.get(id=serializer.data['id']), bio=request.data['profile']['bio'],
                              address=request.data['profile']['address'])
            profile.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return MainUser.objects.all()