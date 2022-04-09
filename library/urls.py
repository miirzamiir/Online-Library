from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, CategoryViewSet, PublisherViewSet, RentViewSet, RequestViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('publishers', PublisherViewSet)
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('requests', RequestViewSet, basename='requests')
router.register('rents', RentViewSet, basename='rents')

urlpatterns = router.urls