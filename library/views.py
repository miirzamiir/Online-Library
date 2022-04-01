from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .filters import AuthorFilter
from .models import Author
from .permissions import IsAdminUserOrReadOnly
from .serializers import AuthorSerializer

class AuthorViewSet(ModelViewSet):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_class = AuthorFilter
    search_fields = ('name',)