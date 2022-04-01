from crypt import methods
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import CreateUserSerializer, ManageUserSerializer


class CreateUserAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class ManageUserAPI(RetrieveUpdateDestroyAPIView):
    
    http_method_names = ['get', 'delete', 'patch']
    serializer_class = ManageUserSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        return self.request.user
