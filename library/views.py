from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .filters import AuthorFilter, BookFilter
from .models import Author, Book, Category, Publisher
from .permissions import IsAdminUserOrReadOnly
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer, PublisherSerializer, RetrieveBookSerializer

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


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'authors__name', 'translators__name', 'publisher__name')
    filter_class = BookFilter

    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return RetrieveBookSerializer
        
        return BookSerializer

