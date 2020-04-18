from rest_framework import serializers

from TODO._auth.models import  MainUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = MainUser
        fiels = ('id','username','is_superuser','password',)


    def create(self,validated_data):
        user = MainUser.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user