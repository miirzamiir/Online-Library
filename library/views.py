from venv import create
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .filters import AuthorFilter, BookFilter
from .models import Author, Book, Category, Publisher, Request
from .permissions import AdminUserCantPOST, IsAdminUserOrReadOnly
from .serializers import AdminRequestSerializer, AuthorSerializer, BookSerializer, CategorySerializer,\
                         GetRequestSerializer, PublisherSerializer, RequestSerializer,\
                         RetrieveBookSerializer

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

    queryset = Book.objects.select_related('publisher').prefetch_related('authors', 'translators', 'categories').all()
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'authors__name', 'translators__name', 'publisher__name')
    filter_class = BookFilter

    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return RetrieveBookSerializer
        
        return BookSerializer


class RequestViewSet(ModelViewSet):


    permission_classes = (IsAuthenticated, AdminUserCantPOST)

    def get_queryset(self):
        
        queryset = Request.objects.select_related('book').filter(rented=False)

        if not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)

        return queryset

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminRequestSerializer

        if self.request.method == 'POST':
            return RequestSerializer

        return GetRequestSerializer