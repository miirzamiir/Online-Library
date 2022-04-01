from rest_framework import serializers
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'name')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password',}
            }
        }


class ManageUserSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        password = validated_data.pop('password',None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user



    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'email', 'password')
        read_only_fields = ('id',)
        write_only_fields = ('password',)
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password',}
            }
        }

