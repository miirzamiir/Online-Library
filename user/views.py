from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import CreateUserSerializer, ManageUserSerializer


class TokenAPI():
    pass


class CreateUserAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class ManageUserAPI(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ManageUserSerializer

    def get_object(self):
        return self.request.user
