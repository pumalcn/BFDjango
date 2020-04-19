from rest_framework import serializers
from firstlabs.users.models import MainUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

  #for hashing
    def create(self,validated_data):
        user = MainUser.objects.create_user(**validated_data)
        return user 