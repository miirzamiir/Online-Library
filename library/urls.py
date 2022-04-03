from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, PublisherViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('publishers', PublisherViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls