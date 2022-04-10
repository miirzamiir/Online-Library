from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from library.models import BookImage
from .views import AuthorViewSet, BookImageViewSet, BookViewSet, CategoryViewSet, PublisherViewSet, RentViewSet, RequestViewSet

router = DefaultRouter()

router.register('authors', AuthorViewSet)
router.register('publishers', PublisherViewSet)
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('requests', RequestViewSet, basename='requests')
router.register('rents', RentViewSet, basename='rents')

nested_router = NestedSimpleRouter(router, 'books', lookup='book')
nested_router.register('images', BookImageViewSet, basename='book-images')



urlpatterns = router.urls + nested_router.urls