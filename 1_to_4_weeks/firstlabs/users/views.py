from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from firstlabs.users.serializers import UserSerializer
from firstlabs.users.models import MainUser


class RegisterUserAPIView(APIView):
    http_method_names = ['post']


    def post(self,request):
        serializer = UserSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save() нужно ли писать return return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
   ##variable
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        return MainUser.objects.all()