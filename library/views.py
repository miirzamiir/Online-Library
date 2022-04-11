from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .filters import AuthorFilter, BookFilter, RentFilter
from .models import Author, Book, BookImage, Category, Publisher, Rent, Request
from .permissions import AdminUserCantPOST, IsAdminUserOrReadOnly
from .serializers import AdminRequestSerializer, AuthorSerializer, BookImageSerializer, BookSerializer, CategorySerializer,\
                         GetRequestSerializer, PublisherSerializer, RentSerializer, RequestSerializer,\
                         RetrieveBookSerializer, UpdateRentSerializer

class AuthorViewSet(ModelViewSet):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_class = AuthorFilter
    search_fields = ('name',)
    pagination_class = PageNumberPagination
    

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

    queryset = Book.objects.select_related('publisher').prefetch_related('authors', 'translators', 'categories', 'images').all()
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'authors__name', 'translators__name', 'publisher__name')
    filter_class = BookFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return RetrieveBookSerializer
        
        return BookSerializer


class BookImageViewSet(ModelViewSet):

    serializer_class = BookImageSerializer

    def get_queryset(self):
        return BookImage.objects.filter(book=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_id' : self.kwargs['book_pk']}


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
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RentViewSet(ModelViewSet):

    http_method_names = ['get', 'patch']
    serializer_class = RentSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_class = RentFilter

    def get_queryset(self):
        queryset = Rent.objects.select_related('request').order_by('-borrow_date')
        if self.request.user.is_superuser:
            return queryset

        return queryset.filter(request__user=self.request.user)

    def get_serializer_class(self):
        
        if self.request.method == 'PATCH':
            return UpdateRentSerializer
        
        return RentSerializer