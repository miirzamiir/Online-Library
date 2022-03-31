from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import CreateUserSerializer

class CreateUserAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
