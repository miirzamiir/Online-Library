from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .filters import AuthorFilter
from .models import Author, Category, Publisher
from .permissions import IsAdminUserOrReadOnly
from .serializers import AuthorSerializer, CategorySerializer, PublisherSerializer

class AuthorViewSet(ModelViewSet):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_class = AuthorFilter
    search_fields = ('name',)


class PublisherViewSet(ModelViewSet):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'telephone_number', 'address')


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description')